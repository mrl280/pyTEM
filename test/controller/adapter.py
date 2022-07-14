import pathlib
import sys


package_directory = pathlib.Path().resolve()
sys.path.append(str(package_directory))
from pyTEM.Interface import Interface
tem = Interface()

import xbox_python

def xy():
    Cx = tem.get_stage_position()['x']
    Cy = tem.get_stage_position()['y']

    SetX = (xbox_python.joy.read()[0]*10**(-6)) + Cx
    SetY = (xbox_python.joy.read()[1]*10**(-6)) + Cy
    tem.set_stage_position({'x': SetX, 'y': SetY})

def z():
    Cz = tem.get_stage_position()['z']

    SetZ = (xbox_python.joy.read()[4]*10**(-6)) + Cz
    SetZ = (xbox_python.joy.read()[5]*10**(-6)) - Cz
    tem.set_stage_position({'z': SetZ})  

def reset():
    tem.set_stage_position({'x': 0, 'y': 0})
    print('STAGE RESET!')