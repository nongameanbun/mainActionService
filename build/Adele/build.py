from build.Adele.baseBuild import *
from build.Adele.skill import *
from gateway import *


class Adele_Triepe3(Adele_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Adele_Triepe3"
      
    def loop(self) :
        def cycle() :
            for _ in range(8) :
                pos = check_pos()
                if pos[0] > 232 and pos[0] != 1050  :
                    break
                doublejump_R("s")
                order()
            
            reso("up")

            for _ in range(8) :
                pos = check_pos()
                if pos[0] < 81 and pos[0] != 1050  :
                    break
                doublejump_L("s")
                order()
                            
            
        ## 위잉 전체 빌드 ##
        cycle()
        if self.timer.is_time_passed('buff') :
            if self.timer.is_time_passed('exp') :
                for _ in range(3) :
                    press_key_with_delay("num7", 150)
                    Rdelay_2(500)
                    
            Rdelay_2(300)
            press_key_with_delay("insert", 300)
            Rdelay_2(200)
            press_key_with_delay("pagedown", 300)
            Rdelay_2(200)
            self.timer.skill_used('buff')

        ###################

    def elbo(self) :
        if self.timer.is_time_passed('origin') :
            press_key_with_delay(self.buildSystem['originkey'], 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass

class Adele_Limen2_5(Adele_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Adele_Limen2_5"

    def loop(self) :
        def cycle() :
            for _ in range(5) :
                pos = check_pos()
                if pos[0] < 70 and pos[0] != 1050  :
                    break
                doublejump_L("s")
                order()

            for _ in range(5) :
                pos = check_pos()
                if pos[0] > 130 and pos[0] != 1050  :
                    break
                doublejump_R("s")
                order()
     
            
        ## 위잉 전체 빌드 ##
        cycle()

        if self.timer.is_time_passed('fountain') :
            reso("up")
            Rdelay_2(500)
            press_key_with_delay(self.buildSystem['fountain_key'], 100)
            Rdelay_2(500)
            self.timer.skill_used('fountain')

            if self.timer.is_time_passed('exp') :                
                for _ in range(3) :
                    press_key_with_delay("num7", 150)
                    Rdelay_2(500)
            

        if self.timer.is_time_passed('buff') :
            Rdelay_2(300)
            press_key_with_delay("insert", 300)
            Rdelay_2(200)
            press_key_with_delay("pagedown", 300)
            Rdelay_2(200)
            self.timer.skill_used('buff')

        ###################

    def elbo(self) :
        if self.timer.is_time_passed('origin') :
            press_key_with_delay(self.buildSystem['originkey'], 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass

class Adele_FireLib3(Adele_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Adele_FireLib3"

    def loop(self) :
        def cycle() :
            for _ in range(8) :
                pos = check_pos()
                if pos[0] > 140 and pos[0] != 1050  :
                    break
                doublejump_R("s")
                order()
            
            reso("up")

            for _ in range(8) :
                pos = check_pos()
                if pos[0] < 20 and pos[0] != 1050  :
                    break
                doublejump_L("s")
                order()
                            
            
        cycle()
        if self.timer.is_time_passed('buff') :
            if self.timer.is_time_passed('exp') :                
                for _ in range(3) :
                    press_key_with_delay("num7", 150)
                    Rdelay_2(500)
                    
            Rdelay_2(300)
            press_key_with_delay("insert", 300)
            Rdelay_2(200)
            press_key_with_delay("pagedown", 300)
            Rdelay_2(200)
            self.timer.skill_used('buff')

        ###################

    def elbo(self) :
        if self.timer.is_time_passed('origin') :
            press_key_with_delay(self.buildSystem['originkey'], 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass

class Adele_SungMoon_4(Adele_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Adele_SungMoon_4"
        self.pos = [(53, 126)]

    def loop(self) :
        def cycle() :
            
            for i in range(8) :
                pos = check_pos()
                if pos[0] < 60 and pos[0] != 1050  :
                    break
                doublejump_L("s")
                order()
                    
            reso("up")
        
            for i in range(8) :
                pos = check_pos()
                if pos[0] > 160 and pos[0] != 1050  :
                    break
                doublejump_R("s")
                order()
            
        ## 위잉 전체 빌드 ##
        cycle()
        if self.timer.is_time_passed('buff') :
                               
            Rdelay_2(300)
            press_key_with_delay("insert", 300)
            Rdelay_2(200)
            press_key_with_delay("pagedown", 300)
            Rdelay_2(200)
            self.timer.skill_used('buff')

        if self.timer.is_time_passed('fountain') :
            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)
            Rdelay_2(1000)
            prev = check_pos()
            for _ in range(3) :
                press_key_with_delay("up", 200)
                Rdelay_2(800)
                cur = check_pos()
                if prev != cur :
                    break

            Rdelay_2(500)
            press_key_with_delay("left", 30)
            Rdelay_2(500)
            press_key_with_delay(self.buildSystem['fountain_key'], 100)
            Rdelay_2(500)
            self.timer.skill_used('fountain')

            if self.timer.is_time_passed('exp') :
                
                for _ in range(3) :
                    press_key_with_delay("num7", 150)
                    Rdelay_2(500)
        ###################

    def elbo(self) :
        if self.timer.is_time_passed('origin') :
            press_key_with_delay(self.buildSystem['originkey'], 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass

class Adele_Winter_4(Adele_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Adele_Winter_4"
        self.pos = [(39, 101), (166, 101)]

    def loop(self) :

        def clean_meso() :
            if self.timer.is_time_passed('buff') :
                               
                Rdelay(300)
                press_key_with_delay("insert", 300)
                Rdelay(200)
                press_key_with_delay("pagedown", 300)
                Rdelay(200)
                self.timer.skill_used('buff')

            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

            Rdelay_2(500)
            
            try_portal()

            Rdelay_2(200)
            press_key_with_delay("left", 30)
            Rdelay_2(200)
            
            press_key_with_delay(self.buildSystem['fountain_key'], 200)
            Rdelay_2(300)

            try_portal()
            
        def line_drive() :
            for i in range(8) :
                pos = check_pos()
                if pos[0] > 150 and pos[0] != 1050  :
                    break
                doublejump_R("s")
                order()

        def cycle() :
            press_key_with_delay("right", 100)
            
            downjump_key("s")
            Rdelay_2(500)
            if prob(50) :
                line_drive()
                Rdelay_2(500)
            else :
                downjump_key("s")
                Rdelay_2(500)
                line_drive()
            
            for _ in range(4) :
                downjump_key("s")
                Rdelay_2(1000)
                pos = check_pos()
                if pos == self.pos[0] :
                    break


            
                
            
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
