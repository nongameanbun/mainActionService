from fastapi import FastAPI, APIRouter
from runner import start_weeing_process, get_weeing_pid, cleanup_weeing, weeing_lock, running_threads
import threading
from build.FinalBuild import build_map, get_build_system
from utils.position import goto_point
from gateway import *
import uvicorn

app = FastAPI(title="Main Action API", description="메인 동작 제어 서버")

# ───────────── Build API Endpoints ─────────────

build_router = APIRouter(prefix="/build", tags=["Builds"])

@build_router.get("/list", summary="빌드 목록 조회")
def load_build():
    try:
        names = list(build_map.keys())
        return {"resp": 0, "message": "Build loaded.", "data": names}
    except Exception as e:
        return {"resp": -1, "message": str(e)}

# ───────────── Weeing API Endpoints ─────────────

weeing_router = APIRouter(prefix="/weeing", tags=["Weeing Controls"])

@weeing_router.post("/start/{build_name}/{start_hour}/{start_minute}", summary="위잉 시작")
def start_weeing(build_name: str, start_hour: int, start_minute: int):
    # 기존 작업이 있으면 중단
    if build_name not in build_map:
        return {"resp": -1, "message": f"Unknown build: {build_name}"}
    
    build = get_running_build().get("resp", None)
    if build and build == build_name:
        resume_main()
        return {"resp": 0, "message": f"Weeing '{build_name}' is already running. Resuming."}
    
    cleanup_weeing()
    
    def run_build():
        start_weeing_process(build_name, start_hour, start_minute)

    # 새 thread로 빌드 실행
    t = threading.Thread(target=run_build, daemon=True)
    t.start()
    return {"resp": 0, "message": f"Weeing '{build_name}' started in background."}

@weeing_router.post("/pause", summary="위잉 일시정지")
def pause_weeing():
    try:
        resp = add_intr("user pause")
        if resp is None:
            return {"resp": -1, "message": "Failed to send pause interrupt."}
        if resp.get("resp") == -1:
            return {"resp": -1, "message": resp.get("message", "Unknown error")}
    except Exception as e:
        return {"resp": -1, "message": str(e)}

    return {"resp": 0, "message": "Weeing paused."}

@weeing_router.get("/running_build")
def get_running_build():
    with weeing_lock:
        if running_threads:
            return {"resp": running_threads[0], "system" : get_build_system(running_threads[0])}
        else:
            return {"resp": -1, "message": "No build is currently running."}


# ───────────── Process API Endpoints ─────────────

@app.get("/pid", summary="빌드 프로세스 PID 조회")
def get_pid():
    cleanup_weeing()
    pid = get_weeing_pid()
    if pid is None:
        return {"resp": -1, "message": "No running process."}
    return {"resp": pid, "message": f"Current PID: {pid}"}

@app.post("/goto_point", summary="지정 위치로 이동")
def api_goto_point(x:int, y:int, tolerance:int=1):
    try :
        system = get_running_build().get("system", {})
        if not system :
            return {"resp": -1, "message": "No running build system found."}
        goto_point(x, y, tolerance, stack=0, system=system)
        return {"resp": 0, "message": f"Moving to point ({x}, {y}) with tolerance {tolerance}."}
    except Exception as e :
        return {"resp": -1, "message": str(e)}

app.include_router(build_router)
app.include_router(weeing_router)

# ───────────── run app ─────────────

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004, log_level="warning")
