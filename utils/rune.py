import threading
import time

from gateway import *
from utils.position import *

def autorune(stack=0) :
    if(stack >= 4):
        send_message("Autorune failed after 4 attempts.")
        return

    Rdelay_2(100)
    press_key_with_delay("space", 100)

    Rdelay_2(500)

    res = solve_rune()
    print(res)

    if res is None or len(res) != 4 :
        print("Rune solution is not complete. Retrying...")
        time.sleep(4)
        autorune(stack=stack+1)
        return

    for arrow in res:
        press_key_with_delay(arrow, 100)
        Rdelay(200)        
        

def rune_chase(system):
    rune = check_rune()
    if rune!=None:
        print("Rune detected. Moving toward the Rune...")
        
        threading.Thread(target=awake_rune_solver).start()

        goto_point(rune[0], rune[1], tolerance=2, stack=0, system=system)

        press_key_with_delay("down", 300)

        goto_point(rune[0], rune[1], tolerance=2, stack=0, system=system)

        autorune()

        time.sleep(2)
        clear_rune()

        return True
    return False
