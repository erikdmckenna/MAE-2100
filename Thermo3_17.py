"""
@author: Harsha Chelliah
"""

# Estimating Error of Ideal Gas EoS

from CoolProp import CoolProp as CP
import CoolProp.Plots as CPP
import numpy as np
import math
import matplotlib.pyplot as plt

fluid = 'Ammonia'

# part a
T1 = 293.15 # K
D1 = CP.PropsSI('D', 'T', T1, 'Q', 1, fluid )
T2 = 313.15 # K
v1 = 1/D1
P2 = CP.PropsSI('P', 'T', T2, 'D', 1/v1, fluid)
print(P2)

# part b

T1 = 294.3 # K
D1 = CP.PropsSI('D', 'T', T1, 'Q', 1, fluid )
T2 = 322 # K
v1 = 1/D1
P2 = CP.PropsSI('P', 'T', T2, 'D', 1/v1, fluid)
print(P2)