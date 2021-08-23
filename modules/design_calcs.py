#--------------------USER INPUTS------------------------#
#Calculate the Axial Capacity of R.C wall in accordance with AS3600:2018, Section 11 for walls subject to
# in-plane shear forces

#import modules and packages
import modules.inputs as inpts
from modules.inputs import WallDetails, ReinfDetails, DesignLoads
import math


class WallAxialCapacity:
    def __init__(self, phi_factor):
        self.phi_factor = phi_factor
        phi_factor = 0.65

        inpts.wall_details()
        inpts.reinf_details()
        inpts.design_loads()

    def AxialCalc(self):





