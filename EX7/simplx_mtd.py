import numpy as np
from scipy.optimize import linprog

# Example Linear Programming Problem:
# Maximize: 3x + 2y
# Subject to:
#   x + y <= 4
#   2x + y <= 5
#   x, y >= 0

c = [-3, -2]  # Coefficients of the objective function to minimize (-3x - 2y)
A = [[1, 1], [2, 1]]  # Coefficients of the inequality constraints (left-hand side)
b = [4, 5]  # Right-hand side values of the inequality constraints

result = linprog(c, A_ub=A, b_ub=b, method='simplex')
print("Optimal solution:", result.x)
print("Optimal value:", -result.fun)
