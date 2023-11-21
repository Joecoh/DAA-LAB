import numpy as np

def strassen_multiply(A, B):
    n = len(A)

    # Base case: if the matrices are 1x1, perform a standard multiplication
    if n == 1:
        return np.array([[A[0, 0] * B[0, 0]]])

    # Divide matrices into submatrices
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Recursive steps
    P1 = strassen_multiply(A11 + A22, B11 + B22)
    P2 = strassen_multiply(A21 + A22, B11)
    P3 = strassen_multiply(A11, B12 - B22)
    P4 = strassen_multiply(A22, B21 - B11)
    P5 = strassen_multiply(A11 + A12, B22)
    P6 = strassen_multiply(A21 - A11, B11 + B12)
    P7 = strassen_multiply(A12 - A22, B21 + B22)

    # Combine results to form the final product
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Construct the result matrix
    result = np.zeros((n, n))
    result[:mid, :mid] = C11
    result[:mid, mid:] = C12
    result[mid:, :mid] = C21
    result[mid:, mid:] = C22

    return result

# Example usage:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = strassen_multiply(A, B)
print(result)
