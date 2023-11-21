import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_assignment_problem(cost_matrix):
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_indices, col_indices].sum()
    assignment = list(zip(row_indices, col_indices))
    return assignment, total_cost

# Example usage:
cost_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
assignment, total_cost = solve_assignment_problem(cost_matrix)
print("Optimal Assignment:", assignment)
print("Total Cost:", total_cost)
