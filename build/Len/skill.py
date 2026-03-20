from gateway import *

def downjump(): ## 아랫점
    press_key("down")
    Rdelay(130)
    press_key("left_alt")
    Rdelay(120)
    release_key("down")
    Rdelay(30)
    release_key("left_alt")

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

def doublejump_only() :
    for _ in range(2+prob(10)) :
        Rdelay_2(50)
        press_key_with_delay("left_alt", 80)
    Rdelay_2(250)