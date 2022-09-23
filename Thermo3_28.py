from CoolProp import CoolProp as CP

fluid = "water"

# part a

P1 = 2.0 * 10**6
T1 = 537.15

U = CP.PropsSI('U', 'P', P1, 'T', T1, fluid)
print(U/1000)

# part b
P1 = 2.5 * 10**6
T1 = 437.15

U = CP.PropsSI('U', 'P', P1, 'T', T1, fluid)
print(U/1000)

# part c

# part d
P1 = 689476
T1 = 422

H = CP.PropsSI('H', 'P', P1, 'T', T1, fluid)
print(H)

# part e
P1 = 1.5 * 10**6
v1 = 0.2095
D1 = 1/v1

H = CP.PropsSI('H', 'P', P1, 'D', D1, fluid)
print(H/1000)
