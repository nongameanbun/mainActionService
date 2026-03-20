from datetime import datetime
from gateway import *

from utils.rune import rune_chase
from utils.human_exceptions import *
from build.FinalBuild import build_map

import multiprocessing
import threading
import traceback
import gc
import os
import time



weeing_process = None          # multiprocessing.Process
weeing_lock = threading.Lock()
running_threads = []           # 현재 실행 중인 빌드 이름


class BuildRunner():
    def __init__(self, **kwargs):
        self.system = kwargs.get('system', None)

        if not self.system :
            assert False, "[BuildRunner.__init__] ERROR: system parameter is required"

        try :
            self.movement = self.system['movement']
            self.main_attack_key = self.system['main_attack_key']
            self.npc_key = self.system['npc_key']
            self.rope_key = self.system['rope_key']
            self.fountain_key = self.system['fountain_key']
            self.jump_key = self.system['jump_key']
            self.origin_key = self.system['originkey']
            self.skill_key = self.system['skill_key']
            self.inven_key = self.system['inven_key']
            self.battle_statistics_key = self.system['battle_statistics_key']
            self.ascent_key = self.system['ascent_key']
            self.ascent_num = self.system['ascent_num']
            self.doping_key = self.system['doping_key']
            self.millage_key = self.system['millage_key']
            self.elbo_reward_key = self.system['elbo_reward_key']
        except Exception as e :
            assert False, f"[BuildRunner.__init__] ERROR: system parameter missing keys: {e}"

    def rune_solver(self):
        rune_chase(system=self.system)

    def handle_elbo(self, func):
        if get_status('elbo') >= 0.8 :
            func()

    def human_exceptions(self) :
        do_human_exceptions(self.system)

    def preprocess(self):
        """프로세스 진입 후 실행되는 사전 동작 (시간 대기는 포함하지 않음)"""
        Rdelay_2(1000)
        press_key("up")
        Rdelay_2(100)
        release_key("up")
        Rdelay_2(4000)
        press_key_with_delay(self.main_attack_key, 100)

        return True

    def _run(self, running_build):
        running_build.setup()

        try:
            while True:
                self.handle_elbo(running_build.elbo)
                
                self.rune_solver()
                
                self.human_exceptions()

                running_build.loop()

                if running_build.timer.is_time_passed('exp') :
                    Rdelay_2(500)
                    press_key_with_delay(running_build.buildSystem["millage_key"], 200)
                    Rdelay_2(500)
                    for _ in range(2) :
                        press_key_with_delay(running_build.buildSystem["elbo_reward_key"], 200)
                        Rdelay_2(500)

                    cur_cycle = get_exp_cycle()
                    if cur_cycle == 0:
                        set_exp_cycle(10)
                        handle_gohome()
                    else :
                        releaseAll()
                        Rdelay_2(500)
                        press_key_with_delay(running_build.buildSystem["doping_key"], 200)
                        Rdelay_2(300)

                        running_build.timer.skill_used('exp')
                        send_message(f"{cur_cycle} cycle left")

                        set_exp_cycle(cur_cycle-1)
                        

                if prob(10):
                    gc.collect()


        except Exception as error:
            send_message(f"Error in build runner: {error}")
            print(traceback.format_exc())
            stop_agent_jobs()


        finally:
            print("[_run] FINALLY releaseAll()")
            releaseAll()
            print("[_run] EXIT")


def _weeing_worker(build_name: str):
    """multiprocessing.Process의 target — 별도 프로세스에서 실행"""
    print(f"[worker PID={os.getpid()}] Starting build: {build_name}")

    if build_name not in build_map:
        print(f"[worker] ERROR: Unknown build_name '{build_name}'")
        return

    running_build = build_map[build_name]

    build_runner = BuildRunner(
        system=running_build.buildSystem,
    )

    # 외부 서비스 상태 초기화
    reset_external_states()

    # statusChecker 감지 시작
    capture_on()

    on()

    build_runner.preprocess()

    try:
        build_runner._run(running_build)
    except Exception as e:
        send_message(f"Error in build runner: {e}")
        stop_agent_jobs()

    finally:
        print("[worker] FINALLY — resetting all external states")
        reset_external_states()
        print("[worker] EXIT")


def _wait_until_start(start_hour: int | None, start_minute: int | None):
    """지정 시각까지 대기 (프로세스 밖에서 실행 → interruption 영향 없음)"""
    if start_hour is None or start_minute is None:
        return

    print(f"[wait] Waiting until {start_hour:02d}:{start_minute:02d} ...")
    while True:
        now = datetime.now()
        if now.hour == start_hour and now.minute >= start_minute:
            break
        time.sleep(60)
    print("[wait] 시간 도달 → 프로세스 시작")


def start_weeing_process(build_name: str, start_hour: int | None = None, start_minute: int | None = None):
    """빌드를 별도 프로세스로 시작하고 PID를 보관"""
    global weeing_process

    with weeing_lock:
        if weeing_process and weeing_process.is_alive():
            print("[start_weeing_process] Already running")
            return False

    # ── 시간 대기: 프로세스 밖에서 수행 (interruption 영향 없음) ──
    _wait_until_start(start_hour, start_minute)

    with weeing_lock:
        proc = multiprocessing.Process(
            target=_weeing_worker,
            args=(build_name,),
            daemon=True,
        )
        proc.start()
        weeing_process = proc
        running_threads.clear()
        running_threads.append(build_name)
        return True


def get_weeing_pid() -> int | None:
    """현재 빌드 프로세스의 PID 반환 (없으면 None)"""
    with weeing_lock:
        if weeing_process and weeing_process.is_alive():
            return weeing_process.pid
    return None


def cleanup_weeing():
    """프로세스가 이미 죽었으면 정리"""
    global weeing_process
    with weeing_lock:
        if weeing_process and not weeing_process.is_alive():
            weeing_process.join(timeout=1)
            weeing_process = None
            running_threads.clear()
