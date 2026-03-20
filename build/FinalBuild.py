from build.Adele.build import *
from build.Len.build import *
from build.Zero.build import *
from build.Shadower.build import *

build_name_list = ['Len_Winter_4', 'Adele_SungMoon_4']
build_list = [Len_Winter_4(), Adele_SungMoon_4()]

build_map = {}

for name, cls in zip(build_name_list, build_list) :
    build_map[name] = cls

def get_build_system(build_name) :
    build = build_map.get(build_name)
    if build :
        return build.get_system()
    return None