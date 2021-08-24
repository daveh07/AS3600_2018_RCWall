# AS3600_2018_RCWall
Axial and shear capacity calculator for walls subjected to axial and in-plane shear in accordane with AS2600:2018, section 11.

### REPL - View Live CLI Output:
Refer to link below to run the code from Repl.it CLI
https://replit.com/@daveh87/MoCalculator?embed=1#main.py

### Introduction
I am a Structural Engineer from Sydney Australia, i've created a main.py python script to calculate the axial and in-plane shear forces for reinforced concrete walls to Australian Standards  
Refer to example calculation below for input units.

### Setup
Clone the repository:

> $ git clone https://github.com/daveh07/AS3600_2018_RCWall.git

> Py Version: Python 3.9

Create a virtual environment and run main.py

### NOTE:
Please feel free to add any contributions! Further functions to be added for minimum reinforcement outputs. 

### What I Learned
<li>Creating a command line script</li>
<li>Using Repl.it to deploy CLI App</li>
<li>Creating user inputs, creating classes and functions to perform calculations based on input values</li>

### Example Caluclation
3500mm High x 4200mm long x 250mm thick R.C Wall

#### Section Properties:
<li> Wall Height, Hw = 3500mm
<li> Wall Length, Lw = 4200mm
<li> Wall Thickness, tw = 250mm
<li> Effective Height Factor, k = 1.0
<li> Concrete Strength, f'c = 40MPa
<li> Concrete Density, yc = 25kN/m3
<li> Wall Braced.. (str) = 1
<li> Wall Structure Over (str) = 1

#### Reinforcement Details:
<li> Yield Strength of Reinforcement, fsy (MPa) = 500
<li> Clear Cover to Reinforcement, C (mm) = 30
<li> No. of  Reinforcement Layers: 2
<li> Vertical Reinforcement dia.(mm): 16
<li> Vertical Reinforcement Spacing (mm): 200
<li> Horizontal Reinforcement dia.(mm): 12
<li> Horizontal Reinforcement Spacing (mm): 200
<li> Reinfrocement Type (str): N
<li> Degree of Crack Control (str): moderate 
<li> Exposure Classification (str): 1

#### Design Loads:
Axial Design Load, N* (kN/m) = 1850
Shear Force Design Load, V* (kN/m) = 550

#### Results:
<li> Axial Capicity = 3054.48kN/m  
<li> Shear Capacity = 3133.66kN/m  


