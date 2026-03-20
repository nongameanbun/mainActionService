from build.Zero.baseBuild import *
from build.Zero.skill import *
from gateway import *
from utils.position import *


class Zero_Winter_4(Zero_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Zero_Winter_4"
        self.meso_right = True
        self.rune_solved = True
        self.doping_key = "f12"
        self.pos = [(55, 116)]


    def loop(self) :
        def cycle() :
            press_key_with_delay(self.buildSystem['main_attack_key'], 2000)

            for i in range(3) :
                press_key_with_delay("w", 100)
                Rdelay_2(300)

            if self.timer.is_time_passed('meso') :
                press_key_with_delay("left", 1000)
                Rdelay_2(200)
                press_key_with_delay("right", 1000)
                self.timer.skill_used('meso')
            
            Rdelay_2(100)
            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 2, system=self.buildSystem)
            Rdelay_2(1000)
            press_key_with_delay("right", 50)
            Rdelay_2(1500)
            
            Rdelay_2(600)

            if check_rune() :
                self.rune_solved = False
                press_key_with_delay("q", 500)
                Rdelay_2(500)

            press_key_with_delay("f", 1200)
            Rdelay_2(1200)

        
        if not self.rune_solved :
            press_key_with_delay("q", 100)
            Rdelay_2(500)
            self.rune_solved = True

        cycle()

        

        if self.timer.is_time_passed('fountain'):
            self.timer.skill_used('fountain')

            

            Rdelay_2(400)
            press_key_with_delay("q", 300)
            Rdelay_2(400)

            move_tel("down")

            flash_assault()
            Rdelay_2(300)
            

            move_tel("right")
            Rdelay_2(300)
            
            
            rolling_curve()
            
            Rdelay_2(800)
            releaseAll()
            Rdelay_2(300)

            move_tel("up")

            Rdelay_2(100)
            press_key_with_delay("up", 700)

            Rdelay_2(100)
            press_key_with_delay("left", 50)
            Rdelay_2(100)
            press_key_with_delay(self.buildSystem['fountain_key'], 500)
            Rdelay_2(100)

            flash_assault()
            Rdelay_2(200)

            move_tel("left")

            Rdelay_2(500)

            rolling_curve()
            Rdelay_2(1000)
            releaseAll()
            Rdelay_2(500)

            
            
            
            press_key_with_delay("q", 200)
            press_key_with_delay("q", 200)
            Rdelay_2(500)
            press_key_with_delay("right", 50)
            Rdelay_2(500)

            
        if self.timer.is_time_passed('buff'):
            Rdelay_2(300)
            press_key_with_delay("insert", 300)
            Rdelay_2(200)
            press_key_with_delay("pagedown", 300)
            self.timer.skill_used('buff')

    def elbo(self) :
        if self.timer.is_time_passed('origin') :
            press_key_with_delay(self.buildSystem['originkey'], 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass