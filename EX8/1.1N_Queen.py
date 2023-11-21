def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n, result):
    if row == n:
        result.append(["".join(["Q" if col == 1 else "." for col in row]) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, result)
            board[row][col] = 0  # Backtrack

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    result = []
    solve_n_queens_util(board, 0, n, result)
    return result

# Example usage:
n_queens_result = solve_n_queens(4)
for solution in n_queens_result:
    for row in solution:
        print(row)
    print()
