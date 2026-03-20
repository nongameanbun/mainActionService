from build.Shadower.baseBuild import *
from build.Shadower.skill import *
from gateway import *
from utils.position import *


class Shadower_FireLib3(Shadower_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Shadower_FireLib3"
        self.dash = 4
        self.timer.adding_skills('petFood', 1810)

    def reso(self, direction):
        if self.dash > 0 :
            press_key_with_delay("left", 100)
            Rdelay_2(100)
            press_key_with_delay(self.buildSystem['jump_key'], 100)
            Rdelay_2(150)
            press_key_with_delay(self.buildSystem['jump_key'], 100)
            Rdelay_2(30)
            press_two_key(direction, "w")
            Rdelay_2(300)
            Rdelay_2(100)

            if self.dash == 4 :
                self.timer.skill_used('dash')
            
            self.dash -= 1
        else :
            press_key_with_delay("left", 100)
            Rdelay_2(100)
            press_key_with_delay(self.buildSystem['jump_key'], 100)
            Rdelay_2(150)
            press_key_with_delay(self.buildSystem['jump_key'], 100)
            Rdelay_2(30)
            press_key_with_delay("x", 200)
            Rdelay_2(1000)


    def loop(self) :
        def cycle() :
            for i in range(8) :
                pos = check_pos()
                if pos[0] > 150 and pos[0] != 1050  :
                    break
                doublejump_R("s")
                meic()
            
            self.reso("up")

            if self.timer.is_time_passed('fountain') :
                Rdelay_2(1000)
                press_key_with_delay("num4", 100)
                Rdelay_2(500)
                self.timer.skill_used('fountain')

            for i in range(8) :
                pos = check_pos()
                if pos[0] < 20 and pos[0] != 1050  :
                    break
                doublejump_L("s")
                meic()
                            
            
        ## 위잉 전체 빌드 ##
        cycle()

        if self.timer.is_time_passed('petFood') :
            for _ in range(3) :
                press_key_with_delay("num7", 150)
                Rdelay_2(500)
            self.timer.skill_used('petFood')
            
        if self.timer.is_time_passed('dash') :
            self.dash = 4
            
        if self.timer.is_time_passed('buff') :
            if self.timer.is_time_passed('exp') :
                for _ in range(3) :
                    press_key_with_delay("num7", 150)
                    Rdelay_2(500)
                    
            Rdelay_2(300)
            press_key_with_delay("num2", 300)
            Rdelay_2(200)
            self.timer.skill_used('buff')

        ###################

    def elbo(self) :
        if self.timer.is_time_passed('origin') :
            press_key_with_delay(self.buildSystem['originkey'], 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass

