from build.Lete.baseBuild import *
from build.Lete.skill import *
from gateway import *
from utils.position import *


class Lete_Firelib3(Lete_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Lete_Firelib3"
        self.deadspot = [860, 242]
        self.pos = [(94, 117)]

    def loop(self) :
        def _tel_with_count(direction, count) :
            tel_with_count(direction, count, self.buildSystem['tel_key'], self.buildSystem['main_attack_key'])
        def clean_meso() :
            if self.timer.is_time_passed('buff') :
                Rdelay_2(300)
                press_key_with_delay("e", 300)
                Rdelay_2(200)
                self.timer.skill_used('buff')

            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

            _tel_with_count("left", 1)
            _tel_with_count("up", 1)
            _tel_with_count("left", 1)
            _tel_with_count("down", 1)
            _tel_with_count("left", 1)
            goto_point(45, 117, tolerance = 3, system=self.buildSystem)

            _tel_with_count("down", 1)

            goto_point(45, 134, tolerance = 2, system=self.buildSystem)

            _tel_with_count("right", 6)
            goto_point(155, 134, tolerance = 3, system=self.buildSystem)

            _tel_with_count("up", 2)
            goto_point(155, 98, tolerance = 3, system=self.buildSystem)

            _tel_with_count("left", 4)

            _tel_with_count("down", 1)

            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

        def seq_gen() :
            if prob(50) :
                return ["left", "right"]
            else :
                return ["up", "down"]

        def cycle() :

            if prob(30) :
                goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

            if prob(20) :
                gen = seq_gen()
                _tel_with_count(gen[0], 1)
                _tel_with_count(gen[1], 1)
            else :
                for _ in range(6+4*prob(50)+2*prob(25)+prob(10)) :
                    press_key_with_delay("s", 60)
                    Rdelay_2(100)


            Rdelay_2(500)
            if self.timer.is_time_passed('edict') :
                press_key_with_delay("q", 100)
                Rdelay_2(500)
                press_key_with_delay("w", 100)
                Rdelay_2(500)
                press_key_with_delay("num8", 100)
                Rdelay_2(500)
                press_key_with_delay("num9", 100)
                Rdelay_2(500)
                self.timer.skill_used('edict')
            
            if self.timer.is_time_passed('overlad') :
                press_key_with_delay("a", 100)
                Rdelay_2(500)
                press_key_with_delay("d", 100)
                Rdelay_2(500)
                press_key_with_delay("f", 100)
                Rdelay_2(500)
                self.timer.skill_used('overlad')
                
            
        ## 위잉 전체 빌드 ##
        cycle()
        if self.timer.is_time_passed('meso') :
            ## 회수빌드 ##
            clean_meso()

            #############       
            self.timer.skill_used('meso')

        ###################

    def elbo(self) :
        if self.timer.is_time_passed('origin') :
            press_key_with_delay("num4", 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass


class Lete_Winter4(Lete_Build) :
    def __init__(self) :
        super().__init__()
        self.name = "Lete_Winter4"
        self.deadspot = [905, 341]
        self.pos = [(100, 116)]

    def loop(self) :
        def _tel_with_count(direction, count) :
            tel_with_count(direction, count, self.buildSystem['tel_key'], self.buildSystem['main_attack_key'])
        
        def clean_meso0() :
            if self.timer.is_time_passed('buff') :
                Rdelay_2(300)
                press_key_with_delay("e", 300)
                Rdelay_2(200)
                self.timer.skill_used('buff')

            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

        def clean_meso1_1() :
            _tel_with_count("left", 1)
            _tel_with_count("up", 1)
            _tel_with_count("left", 1)
            _tel_with_count("down", 1)
            _tel_with_count("left", 2)
            _tel_with_count("down", 1)

            goto_point(34, 130, tolerance = 3, system=self.buildSystem)

            downjump()
            press_key_with_delay("right", 50)
            Rdelay_2(1000)
            press_key_with_delay(self.buildSystem['fountain_key'], 200)
            Rdelay_2(500)

            prev = check_pos()
            for i in range(3) :                
                press_key_with_delay("up", 200)
                Rdelay_2(800)
                cur = check_pos()
                if prev != cur :
                    break

            _tel_with_count("left", 2)
            _tel_with_count("down", 1)
            _tel_with_count("right", 1)
            _tel_with_count("down", 1)

            goto_point(157, 130, tolerance = 3, system=self.buildSystem)
            downjump()

            Rdelay_2(1000)
        
        def clean_meso1_2() :
            _tel_with_count("left", 1)
            _tel_with_count("up", 1)
            _tel_with_count("left", 1)
            _tel_with_count("left", 2)
            _tel_with_count("down", 1)
            _tel_with_count("down", 1)

            goto_point(34, 130, tolerance = 3, system=self.buildSystem)

            downjump()
            press_key_with_delay("right", 50)
            Rdelay_2(1000)
            press_key_with_delay(self.buildSystem['fountain_key'], 200)
            Rdelay_2(500)

            prev = check_pos()
            for i in range(3) :                
                press_key_with_delay("up", 200)
                Rdelay_2(800)
                cur = check_pos()
                if prev != cur :
                    break

            _tel_with_count("left", 2)
            _tel_with_count("down", 1)
            _tel_with_count("right", 1)
            _tel_with_count("down", 1)

            goto_point(157, 130, tolerance = 3, system=self.buildSystem)
            downjump()

            Rdelay_2(1000)

        def clean_meso2_1() :
            _tel_with_count("right", 1)
            _tel_with_count("down", 1)
            _tel_with_count("right", 3)
            

            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

        def clean_meso2_2() :
            _tel_with_count("down", 1)
            _tel_with_count("right", 4)
            

            goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

        def clean_meso() :
            clean_meso0()
            if prob(50) :
                clean_meso1_1()
            else :
                clean_meso1_2()

            if prob(50) :
                clean_meso2_1()
            else :
                clean_meso2_2()

        def seq_gen() :
            if prob(50) :
                return ["left", "right"]
            else :
                return ["up", "down"]

        def cycle() :

            if prob(30) :
                goto_point(self.pos[0][0], self.pos[0][1], tolerance = 1, system=self.buildSystem)

            if prob(20) :
                gen = seq_gen()
                _tel_with_count(gen[0], 1)
                _tel_with_count(gen[1], 1)
            else :
                for _ in range(6+4*prob(50)+2*prob(25)+prob(10)) :
                    press_key_with_delay("s", 60)
                    Rdelay_2(100)


            Rdelay_2(500)
            if self.timer.is_time_passed('edict') :
                press_key_with_delay("q", 100)
                Rdelay_2(500)
                press_key_with_delay("w", 100)
                Rdelay_2(500)
                press_key_with_delay("num8", 100)
                Rdelay_2(500)
                press_key_with_delay("num9", 100)
                Rdelay_2(500)
                self.timer.skill_used('edict')
            
            if self.timer.is_time_passed('overlad') :
                press_key_with_delay("a", 100)
                Rdelay_2(500)
                press_key_with_delay("d", 100)
                Rdelay_2(500)
                press_key_with_delay("f", 100)
                Rdelay_2(500)
                self.timer.skill_used('overlad')
                
            
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
            press_key_with_delay("num4", 100)
            Rdelay_2(7000)
            self.timer.skill_used('origin')
        pass
