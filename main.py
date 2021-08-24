from modules import design_calcs
from modules.design_calcs import *


AxialCheck = design_calcs.WallAxialCapacity()

shearCheck = design_calcs.WallShearCapacity()

print(str(round((AxialCheck.AxialCalc()), 2)) + "kN/m")
print(str(round((shearCheck.ShearCalc()), 2)) + "kN/m")
