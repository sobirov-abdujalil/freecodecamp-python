# Certification Project: Implement the Tower of Hanoi Algorithm
def tower_of_hanoi(n, source, auxiliary, target, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append((source, target))
    else:
        tower_of_hanoi(n - 1, source, target, auxiliary, moves)
        moves.append((source, target))
        tower_of_hanoi(n - 1, auxiliary, source, target, moves)
    return moves

def print_moves(moves):
    for i, (src, dst) in enumerate(moves, 1):
        print(f"Move {i}: {src} -> {dst}")
    print(f"Total moves: {len(moves)}")

n = 3
moves = tower_of_hanoi(n, "A", "B", "C")
print(f"Tower of Hanoi with {n} disks:")
print_moves(moves)
