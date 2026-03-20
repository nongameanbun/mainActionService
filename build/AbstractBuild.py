import time

class Timer:
    def __init__(self):
        self.time_records = {}
        self.cooltime_records = {}
        
    def adding_skills(self, skill_name, cooltime):
        self.cooltime_records[skill_name] = cooltime
        
    def initialization(self):
        for key, value in self.cooltime_records.items():
            self.time_records[key] = 0
        print(self.cooltime_records)
    
    def is_time_passed(self, skill_name):
        current = time.time()
        cooltime = self.cooltime_records[skill_name]
        if(self.time_records[skill_name]==0 or (current - self.time_records[skill_name] > cooltime)):
            return True
        return False
    
    def is_time_passed_delay(self, skill_name, delay):
        current = time.time()
        cooltime = self.cooltime_records[skill_name]
        if(self.time_records[skill_name]==0 or (current - self.time_records[skill_name] > delay)):
            return True
        return False
    
    def skill_used(self, skill_name):
        current = time.time()
        self.time_records[skill_name] = current

class AbstractBuild() :
    def __init__(self) :
        self.buildName = ""
        
        self.buildSystem = {}
        self.skillMotion = {}
        self.timer = Timer()

    def get_system(self) :
        return self.buildSystem
        
    def setup(self) :
        pass

    def loop(self) :
        pass

    def elbo(self) :
        pass