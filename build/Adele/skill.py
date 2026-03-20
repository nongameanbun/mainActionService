from gateway import *
from utils.position import *


def order() :
    Rdelay_2(50)
    if prob(20) :
        if prob(5) :
            press_key_with_delay("f", 100)
        elif prob(5) :
            press_key_with_delay("x", 100)
        elif prob(10) :
            press_key_with_delay("y", 100)
        else :
            press_key_with_delay("a", 100)
    else :
        Rdelay_2(100)
    Rdelay_2(100)
    

def reso(direction):
    press_key(direction)
    press_key_with_delay("e", 100)
    Rdelay_2(200)
    press_key_with_delay("w", 50)
    Rdelay_2(50)
    press_key_with_delay("w", 100)
    Rdelay_2(100)
    press_key_with_delay("w", 100)
    Rdelay_2(100)
    release_key(direction)
    Rdelay_2(250)


def doublejump(dir, command_key) :
    assert not (dir != "left" and dir != "right") ## assert False when unexpected direction detected
    
    press_key(dir) ## set direction
    for i in range(2) : ## push jump 3 times
        Rdelay_2(30)
        press_key_with_delay("left_alt", 80)
    
    if prob(50) :
        release_key(dir) ## give random of the time pressing direction key
        
        Rdelay_2(50)
        press_key_with_delay(command_key, 150)
        Rdelay_2(200)

    else :
        press_key_with_delay(command_key, 150)
        Rdelay_2(100)   
        release_key(dir)
        Rdelay_2(200)

def doublejump_L(command_key) :
    doublejump("left", command_key)
    
def doublejump_R(command_key) :
    doublejump("right", command_key)
    
def downjump():
    press_key("down")
    Rdelay(130)
    press_key("left_alt")
    Rdelay(120)
    release_key("down")
    Rdelay(30)
    release_key("left_alt")
def downjump_key(command_key): ## 아랫점과 동시에 key한번 누르기
    try :
        press_key("down")
        Rdelay(130)
        press_key("left_alt")
        Rdelay(120)
        release_key("down")
        Rdelay(30)
        press_key(command_key)
        Rdelay_2(80)
        release_key("left_alt")
        Rdelay_2(25)
        release_key(command_key)
    except Exception as e:
        print(e)

def try_portal() :
    prev = check_pos()
    for _ in range(3) :                
        press_key_with_delay("up", 200)
        Rdelay_2(800)
        cur = check_pos()
        if prev != cur :
            break