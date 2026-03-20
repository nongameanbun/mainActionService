from build.AbstractBuild import *
from gateway import *

class Shadower_Build(AbstractBuild) :
    def __init__(self) :
        super().__init__()
        self.timer = Timer()
        self.buildSystem = {
            "movement" : "jump2",
            "main_attack_key" : "s",
            "doping_key" : "f12",
            
            "npc_key" : "space",
            "rope_key" : "x",
            "fountain_key" : "num6",
            "jump_key" : "left_alt",

            "originkey" : "num8",
            "skill_key" : "k",
            "inven_key" : "i",
            "battle_statistics_key" : "num_minus",
            "ascent_key" : "f3",
            "ascent_num" : 0,

            "dead_potion_key" : "f6",
            "millage_key" : "f7",
            "elbo_reward_key" : "f8",
        }
    
    def setup(self) :
        self.timer.adding_skills('buff', 120)
        self.timer.adding_skills('fountain', 57.6)
        self.timer.adding_skills('origin', 600)
        self.timer.adding_skills('exp', 1810)
        self.timer.adding_skills('meso', 110)
        self.timer.adding_skills('dash', 60)
        self.timer.initialization()
        press_key_with_delay("num1", 50)
        time.sleep(1)
