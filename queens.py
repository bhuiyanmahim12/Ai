N = 8  # Number of queens
solution_count = 0  # count solutions globally

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print("\n")

def is_safe(board, row, col):
    # Check this row on left
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_nq_util(board, col):
    global solution_count
    # If all queens are placed
    if col >= N:
        print_solution(board)
        solution_count += 1
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nq_util(board, col + 1) or res
            board[i][col] = 0  # Backtrack
    return res

def solve_nq():
    global solution_count
    board = [[0] * N for _ in range(N)]
    if not solve_nq_util(board, 0):
        print("No solution exists")
    else:
        print(f"Total number of solutions: {solution_count}")

# Run the program
solve_nq()
