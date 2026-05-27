# Lab: Implement the N-Queens Problem
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions

def print_solution(solution):
    n = len(solution)
    for row in solution:
        line = [". "] * n
        line[row] = "Q "
        print("".join(line))
    print()

n = 4
solutions = solve_n_queens(n)
print(f"{n}-Queens has {len(solutions)} solutions:")
for sol in solutions:
    print_solution(sol)
