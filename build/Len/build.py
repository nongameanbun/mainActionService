from build.Len.baseBuild import *
from build.Len.skill import *
from gateway import *
from utils.position import *


class Len_Sungmoon4(Len_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Len_Sungmoon4"
        self.pos = [(53, 126)]
        self.state = False

    def loop(self) :
        def clean_meso() :
            if self.timer.is_time_passed('buff') :
                Rdelay_2(300)
                press_key_with_delay("num1", 300)
                Rdelay_2(200)
                self.timer.skill_used('buff')

            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

            
            prev = check_pos()
            for i in range(3) :                
                press_key_with_delay("up", 200)
                Rdelay_2(800)
                cur = check_pos()
                if prev != cur :
                    break

            Rdelay_2(200)
            press_key_with_delay("left", 30)
            Rdelay_2(200)
            
            press_key_with_delay("a", 200)
            Rdelay_2(300)

            prev = check_pos()
            for i in range(3) :                
                press_key_with_delay("up", 200)
                Rdelay_2(800)
                cur = check_pos()
                if prev != cur :
                    break
            
            press_key_with_delay("right", 100)
            Rdelay_2(200)
            press_key_with_delay(self.buildSystem['fountain_key'], 200)
            Rdelay_2(500)

            if prob(50):
                doublejump_L("s")
                Rdelay_2(200)
        
        def cycle() :
            press_key_with_delay("right", 100)
            Rdelay_2(100)

            if prob(70):
                if self.timer.is_time_passed('manghon') :
                    for i in range(4) :                    
                        doublejump_R("q")
                        Rdelay_2(250)
                    self.timer.skill_used('manghon')
                Rdelay_2(500)

            # if not self.state :
            press_key("s")
            self.state = True
            for i in range(8) :
                # print(f"doublejump: {i}")
                verify_position()
                pos = check_pos()
                if pos[0] > 160 and pos[0] != 1050  :
                    break
                
                doublejump_only()
                Rdelay_2(200)
            
            if prob(20) :
                release_key("s")
                self.state = False
           

            if self.timer.is_time_passed('meso') :
                goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)
                Rdelay_2(500)
                press_key_with_delay("up", 100)
                Rdelay_2(500)
                self.timer.skill_used('meso')

            Rdelay_2(300)
            press_key_with_delay("left", 100)
            Rdelay_2(100)

            if prob(70):
                if self.timer.is_time_passed('manghon') :
                    for i in range(4) :                    
                        doublejump_L("q")
                        Rdelay_2(200)
                    self.timer.skill_used('manghon')
                Rdelay_2(500)

            # if not self.state :
            press_key("s")
            self.state = True
            for i in range(8) :
                verify_position()
                pos = check_pos()
                if pos[0] < 30  :
                    break
                
                doublejump_only()
                # print(f"doublejump: {i}")
                Rdelay_2(300)
            if prob(20) :
                release_key("s")
                self.state = False
                
            
        ## 위잉 전체 빌드 ##
        cycle()
        if self.timer.is_time_passed('fountain') :
            ## 회수빌드 ##
            clean_meso()

            #############       
            self.timer.skill_used('fountain')

        ###################

    def elbo(self) :
        if self.timer.is_time_passed('origin') :
            press_key_with_delay("num2", 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass

class Len_Winter_4(Len_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Len_Winter_4"
        self.pos = [(39, 101), (166, 101)]

    def loop(self) :

        def clean_meso() :
            if self.timer.is_time_passed('buff') :
                Rdelay_2(300)
                press_key_with_delay("num1", 300)
                Rdelay_2(200)
                self.timer.skill_used('buff')

            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

            press_key_with_delay("right", 50)
            Rdelay_2(200)
            press_key_with_delay(self.buildSystem['fountain_key'], 200)
            Rdelay_2(500)
            
            prev = check_pos()
            for i in range(3) :                
                press_key_with_delay("up", 200)
                Rdelay_2(800)
                cur = check_pos()
                if prev != cur :
                    break

            Rdelay_2(200)
            press_key_with_delay("left", 30)
            Rdelay_2(200)
            
            press_key_with_delay("a", 200)
            Rdelay_2(300)

            prev = check_pos()
            for i in range(3) :                
                press_key_with_delay("up", 200)
                Rdelay_2(800)
                cur = check_pos()
                if prev != cur :
                    break
            
        def line_drive() :
            
            if prob(70):
                release_key("s")
                if self.timer.is_time_passed('manghon') :
                    for i in range(4) :                    
                        doublejump_R("q")
                        Rdelay_2(250)
                    self.timer.skill_used('manghon')
                Rdelay_2(500)
                press_key("s")

            for i in range(8) :
                pos = check_pos()
                if pos[0] > 150 and pos[0] != 1050  :
                    break
                
                doublejump_only()
                Rdelay_2(250)

        def cycle() :
            press_key_with_delay("right", 100)
            Rdelay_2(100)
            press_key("s")
            Rdelay_2(500)
            downjump()
            Rdelay_2(500)
            if prob(50) :
                line_drive()
                Rdelay_2(500)
            else :
                downjump()
                Rdelay_2(500)
                line_drive()
            
            for _ in range(4) :
                downjump()
                verify_position()
                pos = check_pos()
                if tuple(pos) == self.pos[0] :
                    break
            
            release_key("s")

            
                
            
        ## 위잉 전체 빌드 ##
        cycle()
        if self.timer.is_time_passed('fountain') :
            ## 회수빌드 ##
            clean_meso()

            #############       
            self.timer.skill_used('fountain')       

        ###################

    def elbo(self) :
        if self.timer.is_time_passed('origin') :
            press_key_with_delay("num2", 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass
