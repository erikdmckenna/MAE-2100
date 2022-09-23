from CoolProp import CoolProp as CP

fluid = "water"

T = 673.15
P = 100 * 10**5
D = CP.PropsSI('D', 'T', T, 'P', P, fluid)
v = 1/D
print(v*2)