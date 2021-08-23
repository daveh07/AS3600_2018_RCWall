#--------------------USER INPUTS------------------------#
#--------------------Wall Properties------------------------#
class WallDetails:
    def __init__(self):
        Hw = float(input("Wall Height (mm), Hw = "))
        Lw = float(input("Wall Length (mm), Lw = "))
        tw = float(input("Wall Thickness (mm), tw = "))
        k = float(input("Effective Height Factor, k = "))
        fc = float(input("Concrete Strength (MPa), fc = "))
        yc = float(input("Concrete Density (kN/m3), yc = "))

        wall_braced = input("Wall Braced & subjected to in-plane load effects only (1),  Wall Braced & subjected to "
                            "in-plane & out-of-plane load effects (2),  Wall is Unbraced (U) - Choose: 1, 2 or U")

        struct_over = input("Wall structure over = Cast In Situ Concrete Floor Continuous Over Wall (1) or"
                            " Discontinuous Floor Over Wall (2) - Choose: 1 or 2")

#--------------------Reinforcement Details------------------------#
class ReinfDetails:
    def __init__(self):
        fsy = float(input("Yeild Strength of Reinforcement, fsy = "))
        C = float(input("Cover to reinforcement (mm), C = "))
        no_of_layers = int(input("Number of reinforcement Layers, 1 or 2 = "))
        vert_reinf = float(input("Vertical Reinforcement Dia.(mm) Size, EG. N12's = 12, N16's = 16, etc"))

        vert_reinf_spacing = float(input("Spacing of Vertical Reinforcement (mm) = "))

        horiz_reinf = float(input("Horizontal Reinforcement Dia.(mm) Size, EG. N12's = 12, N16's = 16, etc"))

        horiz_reinf_spacing = float(input("Spacing of Horizontal Reinforcement (mm) = "))

        reinf_type = input("Normal Ductility or Low Ductility (N/L)")

        c_control = input("Degree of Crack Control: choose - minor, moderate, strong")

        exp_class = input("Exposure Class: A1/A2 (1) or B1/B2/C1/C2 (2)")


#--------------------Design Loads------------------------#
class DesignLoads:
    def __init__(self):
        Nd = float(input("Design Axial Force (kN), N* = "))

        Vd = float(input("Design In-Plane Shear Force (kN), V* = "))


wall_details = WallDetails()
reinf_details = ReinfDetails()
design_loads = DesignLoads()


