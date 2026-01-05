from pulp import *

# -------------------------------
# Step 1: Create LP model
# -------------------------------
model = LpProblem("Chebyshev_Center_MaxBall", LpMaximize)

# -------------------------------
# Step 2: Decision variables (centre coordinates)
# -------------------------------
c1 = LpVariable('c1')
c2 = LpVariable('c2')
c3 = LpVariable('c3')
c4 = LpVariable('c4')

# Radius
r = LpVariable('r', lowBound=0)  # r >= 0

# -------------------------------
# Step 3: Objective function
# -------------------------------
model += r  # maximize radius

# -------------------------------
# Step 4: Constraints
# Use c variables and -2*r as RHS
# -------------------------------

model += c1 + c2 + c3 - c4 - 4 <= -2*r
model += c1 + c2 + c3 - c4 + 4 >= 2*r

model += c1 + c2 - c3 + c4 - 4 <= -2*r
model += c1 + c2 - c3 + c4 + 4 >= 2*r

model += c1 - c2 + c3 + c4 - 4 <= -2*r
model += c1 - c2 + c3 + c4 + 4 >= 2*r

model += -c1 + c2 + c3 + c4 - 4 <= -2*r
model += -c1 + c2 + c3 + c4 + 4 >= 2*r

# -------------------------------
# Step 5: Solve the LP
# -------------------------------
model.solve()

# -------------------------------
# Step 6: Output results
# -------------------------------
print("Status:", LpStatus[model.status])
print("Maximum radius r =", value(r))
print("Centre coordinates chosen by solver:")
print("c1 =", value(c1))
print("c2 =", value(c2))
print("c3 =", value(c3))
print("c4 =", value(c4))
