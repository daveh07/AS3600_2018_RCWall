from modules import design_calcs
from modules.design_calcs import *



AxialCheck = design_calcs.WallAxialCapacity()
ax_check = AxialCheck.AxialCalc()
ax_round = round(ax_check, 2)
ax_str = f"Axial Capacity of Wall Per Metre Run = {ax_round}kN/m"

shearCheck = design_calcs.WallShearCapacity()
sf_check = shearCheck.ShearCalc()
sf_round = round(sf_check, 2)
sf_str = f"Shear Capacity of Wall Per Metre Run = {sf_round}kN/m"

print(ax_str)
print(sf_str)