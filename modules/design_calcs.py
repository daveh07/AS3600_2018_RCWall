# --------------------USER INPUTS------------------------#
# Calculate the Axial Capacity of R.C wall in accordance with AS3600:2018, Section 11 for walls subject to
# in-plane shear forces

# Import modules and packages
import modules.inputs as i
from modules.inputs import *
import math


class WallAxialCapacity:
    def __init__(self, phi_factor):
        super().__init__()
        self.phi_factor = phi_factor
        phi_factor = 0.65

    def AxialCalc(self):
        # Effective Wall Height:
        Hwe = i.Hw * i.k
        # Eccentricity:
        ecc = 0.05*i.tw
        # Additional Eccentricity:
        ecc_add = ((Hwe**2)/(2500*tw))
        # Check Effective Height Ratio:
        eff_h_ratio = Hwe / tw
        # Design Axial Strength of Wall, Phi.Nu:
        phi_Nu = 0.65*((tw - 1.2*ecc-2*ecc_add) * 0.6*i.fc)

    def ShearCalc(self):
        # Shear Strength Excluding Wall Reinforcement
        Vuc = 1
