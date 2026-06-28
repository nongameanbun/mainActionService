from build.AbstractBuild import *
from gateway import *

class Lete_Build(AbstractBuild) :
    def __init__(self) :
        super().__init__()
        self.timer = Timer()
        self.buildSystem = {
            "movement" : "tel",
            "main_attack_key" : "s",
            "doping_key" : "f12",
            
            "npc_key" : "space",
            "rope_key" : "z",
            "fountain_key" : "num6",
            "jump_key" : "left_alt",
            "tel_key" : "left_shift",

            "originkey" : "num2",
            "skill_key" : "k",
            "inven_key" : "i",
            "battle_statistics_key" : "num_minus",
            "ascent_key" : "num5",
            "ascent_num" : 1,

            "dead_potion_key" : "f6",
            "millage_key" : "f7",
            "elbo_reward_key" : "f8",
        }
    
    def setup(self) :
        self.timer.adding_skills('buff', 120)
        self.timer.adding_skills('fountain', 57.6)
        self.timer.adding_skills('origin', 600)
        self.timer.adding_skills('exp', 1810)
        self.timer.adding_skills('edict', 30)
        self.timer.adding_skills('overlad', 60)
        self.timer.adding_skills('meso', 110)
        self.timer.initialization()

        time.sleep(1)

        press_key_with_delay("num8", 100)
        Rdelay_2(500)
        press_key_with_delay("num9", 100)
        Rdelay_2(500)