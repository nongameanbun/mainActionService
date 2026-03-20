import time
from gateway import *
# Handling out-of-range positions.
def handle_outrange_pos() :
    # print("handle_outrange_pos start")
    for _ in range(2):
        me = check_pos()
    _x, _y = me
    if( _y > 1000):
        press_key("left")
        Rdelay_2(700)
        release_key("left")
        Rdelay_2(200)

        me = check_pos()
        _, _y = me
        
        
        if( _y > 1000):
            press_key("right")
            Rdelay_2(700)
            release_key("right")
            Rdelay_2(200)
    
    # print("handle_outrange_pos end")
    
 # Movement functions for far-distance travel.

# Movement functions for far-distance travel.
def do_movement(movement, direction, system) :
    
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
        
    main_attack_key = system['main_attack_key']
    if movement == "jump2" :
        if(direction == "left") :
            doublejump_L(main_attack_key)
        elif(direction == "right") :
            doublejump_R(main_attack_key)
        else :
            assert False, "Invalid Direction"
        return
    
    else :
        assert False, "Not Implemented Movement"

# Verifies the current position.
def verify_position(stack = 0) :
    prev_me = (-1, -1)
    cnt = 0
    while cnt < 2:
        current_me = check_pos()
        if(current_me == prev_me):
            cnt += 1
        else :
            cnt = 0
        prev_me = current_me
        time.sleep(0.03)
    
    if(current_me[1] > 1000):
        if stack == 2 :
            return
        
        time.sleep(0.5)
        verify_position(stack+1)
    
    time.sleep(0.1)
    return

def downjump(): ## 아랫점
    press_key("down")
    Rdelay(130)
    press_key("left_alt")
    Rdelay(120)
    release_key("down")
    Rdelay(30)
    release_key("left_alt")

def goto_point(dest_x, dest_y, tolerance = 2, stack=0, system={}) :
    main_attack_key = system['main_attack_key']
    rope_key = system['rope_key']
    movement = system['movement']
    jump_key = system['jump_key']

    if stack > 3:
        assert False, "Failed to goto_point after multiple retries. Minimap might be blocked or character might be dead."

    if stack > 1:
        Rdelay_2(500)
        press_key("right")
        Rdelay(70)
        press_key(jump_key)
        Rdelay(150)
        press_key(main_attack_key)
        Rdelay(120)
        release_key(main_attack_key)
        Rdelay(60)
        release_key(jump_key)
        Rdelay(150)
        release_key("right")
        Rdelay_2(1500)

    
    if (dest_x > 0 and dest_x < 250 and dest_y > 0 and dest_y < 200):
        releaseAll()
        handle_outrange_pos()
        while True :
                        
            _start = time.time()
            
            # Movement X-axis with big distance error.
            while True:
                # print("big x-axis fitting start")
                if(time.time() - _start > 10):
                    print("Minimap Exception Occured. Retrying..")
                    return goto_point(dest_x, dest_y, tolerance, stack + 1, system)

                for _ in range(2):
                    me = check_pos()
                
                check_x = dest_x - me[0]
                
                if abs(check_x) <= 30:
                    break
                
                if check_x > 30:
                    do_movement(movement, "right", system)

                elif check_x < -30:
                    do_movement(movement, "left", system)

                time.sleep(0.3)
            
            _start = time.time()
            
            # X-axis fitting.
            while True :
                if(time.time() - _start > 10):
                    print("X-axis Exception Occured. Retrying..")
                    return goto_point(dest_x, dest_y, tolerance, stack+1, system)

                handle_outrange_pos()
                
                for _ in range(2):
                    me = check_pos()
                _x, _ = me
                
                # print("small x-axis fitting start")
                check_x = dest_x - _x
                
                if abs(check_x) < tolerance:
                    break

                if check_x > 0:
                    press_key("right")    
                    Rdelay_2(min(1000, 50*abs(check_x)))
                    release_key("right")
                else:
                    press_key("left")
                    Rdelay_2(min(1000, 50*abs(check_x)))
                    release_key("left")
                Rdelay_2(400)      
            
            # Y-axis fitting.
            _start = time.time()
            while True :
                if(time.time() - _start > 10):
                    print("Y-axis Exception Occured. Retrying..")
                    return goto_point(dest_x, dest_y, tolerance, stack + 1, system)

                for _ in range(2):
                    me = check_pos()

                _, _y = me

                check_y = dest_y - _y

                # print("y-axis fitting start")
                if abs(check_y) < 3:         
                    break
                if check_y > 0:
                    downjump()
                    Rdelay_2(400)
                else:
                    # upjump()
                    # Rdelay_2(400)
                    press_key(rope_key)
                    Rdelay_2(200)
                    release_key(rope_key)
                    Rdelay_2(500)
                    press_key_with_delay("up", 400)
                    Rdelay_2(600)
                    
                verify_position()

            me = check_pos()
            check_x = abs(me[0] - dest_x)
            check_y = me[1]-dest_y
            
            if(check_x < tolerance and abs(check_y) < 3 ) :
                return