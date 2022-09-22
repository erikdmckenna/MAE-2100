"""
@author: Harsha Chelliah
"""

# Estimating Error of Ideal Gas EoS

from CoolProp import CoolProp as CP
import CoolProp.Plots as CPP
import numpy as np
import math
import matplotlib.pyplot as plt

# to print out all the fluid substances available in CoolProp database:
print(CP.FluidsList())

fluid = 'Ammonia'

T1 = 293.15 # K
D1 = CP.PropsSI('D', )
T2 = 313.15 # hi