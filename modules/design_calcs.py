# ----------------------DESIGN CALCS------------------------#
# Calculate the Axial Capacity of R.C wall in accordance with AS3600:2018, Section 11 for walls subject to
# in-plane shear forces
#

# Import modules and packages
import math

# ----------------------USER INPUTS--------------------------#
# --------------------Wall Properties------------------------#

Hw = float(input("Wall Height (mm), Hw = "))
Lw = float(input("Wall Length (mm), Lw = "))
tw = float(input("Wall Thickness (mm), tw = "))
k = float(input("Effective Height Factor, k = "))
fc = float(input("Concrete Strength (MPa), fc = "))
yc = float(input("Concrete Density (kN/m3), yc = "))

wall_braced = input("Wall Braced & subjected to in-plane load effects only (1),  Wall Braced & subjected to "
                    "in-plane & out-of-plane load effects (2),  Wall is Unbraced (U):  ")

struct_over = input("Wall structure over = Cast In-Situ Concrete Floor Continuous Over Wall (1) or"
                    " Discontinuous Floor Over Wall (2):  ")

wall_details_dict = {"Hw": Hw,
                     "Lw": Lw,
                     "tw": tw,
                     "k": k,
                     "fc": fc,
                     "yc": yc,
                     "wall_braced": wall_braced,
                     "struct_over": struct_over}


# --------------------Reinforcement Details------------------------#

fsy = float(input("Yeild Strength of Reinforcement, fsy = "))
C = float(input("Cover to reinforcement (mm), C = "))
no_of_layers = int(input("Number of reinforcement Layers, 1 or 2 = "))
vert_reinf = float(input("Vertical Reinforcement Dia.(mm) Size, EG. N12's = 12, N16's = 16:  "))

vert_reinf_spacing = float(input("Spacing of Vertical Reinforcement (mm) = "))

horiz_reinf = float(input("Horizontal Reinforcement Dia.(mm) Size, EG. N12's = 12, N16's = 16:  "))

horiz_reinf_spacing = float(input("Spacing of Horizontal Reinforcement (mm) =  "))

reinf_type = input("Normal Ductility or Low Ductility (N/L):  ")

c_control = input("Degree of Crack Control: choose - minor, moderate, strong:  ")

exp_class = input("Exposure Class: A1/A2 (1) or B1/B2/C1/C2 (2):  ")

reinf_details_dict = {"fsy": fsy,
                       "C": C,
                       "no_of_layers": no_of_layers,
                       "vert_reinf": vert_reinf,
                       "vert_reinf_spacing": vert_reinf_spacing,
                       "horiz_reinf": horiz_reinf,
                       "horiz_reinf_spacing": horiz_reinf_spacing,
                       "reinf_type": reinf_type,
                       "c_control": c_control,
                       "exp_class": exp_class}


# ---------------------Design Loads------------------------#

Nd = float(input("Design Axial Force (kN), N* = "))

Vd = float(input("Design In-Plane Shear Force (kN), V* = "))

design_loads__dict = {"N*": Nd,
                      "V*": Vd}


# ----------------------DESIGN CALCULATIONS--------------------------#

# Calculate Wall Axial Capacity in accordance with AS3600:2018, Section 11 (per unit length)
class WallAxialCapacity:
    def __init__(self):
        super().__init__()

    def AxialCalc(self):
        # Effective Wall Height:
        Hwe = Hw * k
        # Eccentricity:
        ecc = 0.05*tw
        # Additional Eccentricity:
        ecc_add = ((Hwe**2)/(2500*tw))
        # Check Effective Height Ratio:
        eff_h_ratio = Hwe / tw
        # Design Axial Strength of Wall, Phi.Nu:
        phi_Nu = 0.65*((tw - 1.2*ecc-2*ecc_add) * 0.6*fc)
        return phi_Nu

# Calculate Wall In-Plane Shear Capacity in accordance with AS3600:2018, Section 11 (per unit length)
class WallShearCapacity:
    def __init__(self):
        super().__init__()

    def ShearCalc(self): # Shear Strength Excluding Wall Reinforcement CL): 11.6.3
        def Vuc_calc(self):
            if Hw/Lw <= 1.0:
                Vuc = (0.66 * (fc**0.5) - 0.21*(Hw/Lw)*(fc**0.5)) * 0.8 * Lw * tw
            else:
                Vuc = max((0.17 * (fc**0.5)) * 0.8 * Lw * tw, (0.05*(fc**0.5) + ((0.1*fc**0.5)/((Hw/Lw) - 1)))
                          * 0.8 * Lw * tw)
            return Vuc / 1000

        def Pw_calc(self): # Proportion of Wall Reinforcement Contribution CL): 11.6.4
            if Hw/Lw <= 1.0:
                Pw = min((int(no_of_layers * ((vert_reinf / 2)**2)) * math.pi) * (Lw / vert_reinf_spacing) / (Lw * tw),
                        (int(no_of_layers * ((horiz_reinf / 2)**2)) * math.pi) * (Hw / horiz_reinf_spacing) / (Hw * tw))
            else:
                Pw = (int(no_of_layers * (horiz_reinf / 2))**2) * math.pi * (1000 / horiz_reinf_spacing) / (1000 * tw)
            return Pw

        # Create instances
        vuc_calc = Vuc_calc(self)
        pw_calc = Pw_calc(self)

        # Contribution of Wall Reinforcement Contribution CL): 11.6.4
        Vus = pw_calc * fsy * 0.8 * Lw * tw / 1000
        # Maximum Design Shear Strength CL): 11.6.2
        Phi_Vu_max = 0.70 * 0.2 * fc * (0.8 * Lw * tw) / 1000
        # Design Shear Strength of Wall
        Phi_Vu = min(Phi_Vu_max, 0.7 * vuc_calc + 0.7 * Vus)
        return Phi_Vu

# Minimum Reinforcement Requirements for Walls: CL): 11.7
class minReinf:
    def __init__(self):
        super().__init__()

    def horizMin(self):
        if c_control == "minor" and exp_class == "1":
            P = 0.0025
        elif c_control == "moderate":
            P = 0.0035
        else:
            P = 0.006

        if c_control == "minor" and exp_class == "2":
            P = 0.006

        return P

