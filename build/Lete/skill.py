from gateway import *

def downjump(): ## 아랫점
    press_key("down")
    Rdelay(130)
    press_key("left_alt")
    Rdelay(120)
    release_key("down")
    Rdelay(30)
    release_key("left_alt")



def telonly(tel_key, direction) :
    def telonly_left(tel_key) :
        press_key("left")
        Rdelay_2(50)
        press_key_with_delay(tel_key, 50)
        release_key("left")
        Rdelay_2(100)

    def telonly_right(tel_key) :
        press_key("right")
        Rdelay_2(50)
        press_key_with_delay(tel_key, 50)
        release_key("right")
        Rdelay_2(100)

    def telonly_up(tel_key) :
        press_key("up")
        Rdelay_2(50)
        press_key_with_delay(tel_key, 50)
        release_key("up")
        Rdelay_2(100)

    def telonly_down(tel_key) :
        press_key("down")
        Rdelay_2(50)
        press_key_with_delay(tel_key, 50)
        release_key("down")
        Rdelay_2(100)

    if direction == "left" :
        telonly_left(tel_key)
    elif direction == "right" :
        telonly_right(tel_key)
    elif direction == "up" :
        telonly_up(tel_key)
    elif direction == "down" :
        telonly_down(tel_key)
    else :
        assert False, "Invalid Direction"

def tel_with_count(direction, count, tel_key, command_key) :
    for _ in range(count) :
        pos = check_pos()
        for _ in range(2) :
            telonly(tel_key, direction)
            Rdelay_2(50)
            if pos != check_pos() :
                break
        press_key_with_delay(command_key, 150)
        Rdelay_2(100)