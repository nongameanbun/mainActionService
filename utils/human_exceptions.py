
from gateway import *
import random

def handle_go_myster(stack = 0) :
    if stack > 3 :
        send_message("Go Myster Failed.")
        return False

    Rdelay_2(500)
    press_key_with_delay("v", 100)
    Rdelay_2(500)

    detected_result = find_in_screen("mystervil")
    print(f"[handle_go_myster] detected_result: {detected_result}")
    if detected_result is None :
        handle_go_myster(stack + 1)
        return

    x, y = detected_result['center']
    mouse_click('left', 50, x+random.randint(-5, 5), y+random.randint(-2, 2))

    Rdelay_2(500)
    press_key_with_delay("enter", 100)

    Rdelay_2(500)

    press_key_with_delay("v", 100)
    Rdelay_2(500)

    return True


def handle_gohome() :
    
    if handle_go_myster() :
        send_message("Gohome Successful.")
    
    else :
        send_message("Gohome Failed.")
        exit(0)

    exit(0)


def do_human_exceptions(system) :
    battle_statistics_key = system['battle_statistics_key']
    ascent_key = system['ascent_key']
    ascent_num = system['ascent_num']

    if prob(1) and prob(1):
        Rdelay_2(500)
        press_two_key("left_alt", "tab")
        Rdelay_2(5000)
        press_two_key("left_alt", "tab")
        Rdelay_2(500)

    elif prob(1) and prob(10) and battle_statistics_key :
        # print("relog")
        Rdelay_2(200)
        press_key_with_delay("esc", 100)
        Rdelay_2(200)
        press_key_with_delay("enter", 100)
        Rdelay_2(200)
        press_key_with_delay("esc", 100)
        Rdelay_2(200)
        press_key_with_delay("enter", 100)
        Rdelay_2(200)
        press_key_with_delay("esc", 100)
        Rdelay_2(200)
        press_key_with_delay(battle_statistics_key, 100)
        Rdelay_2(200)
        press_key_with_delay(battle_statistics_key, 100)
        Rdelay_2(200)

    elif prob(1) and prob(5) and ascent_key :
        for _ in range(ascent_num) :
            press_key_with_delay(ascent_key, 100)
            Rdelay_2(2000)
