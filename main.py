from modules import design_calcs
from modules.design_calcs import *


def keysPrint():
    a = design_calcs.wall_details_dict.values()
    print(a)

keysPrint()


def AxialCheck():
    N = WallAxialCapacity.AxialCalc(design_calcs.wall_details_dict.values())
    print(N)

AxialCheck()
