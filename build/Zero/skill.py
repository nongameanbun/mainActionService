from gateway import *

def meic() :
    Rdelay_2(50)
    if prob(100) :
        press_key_with_delay("a", 100)
    else :
        Rdelay_2(100)
    Rdelay_2(100)

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
    
def flash_assault():
    for i in range(2 + prob(30)):
        press_key_with_delay("s", 100)
        Rdelay_2(80)
    Rdelay_2(150)

def rolling_curve() :
    press_key_with_delay("d", 1000)
    Rdelay_2(400)

def move_tel(dir) :
    dir_dict = {"left" : "left", "right" : "right", "up" : "up", "down" : "down"}
    Rdelay_2(50)
    press_key(dir_dict[dir])
    Rdelay_2(50)
    press_key_with_delay("left_shift", 50)
    Rdelay_2(50)
    release_key(dir_dict[dir])
    Rdelay_2(50)