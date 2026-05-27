# Lab: Build an Nth Fibonacci Number Calculator
def nth_fibonacci(n):
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

def fibonacci_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

for i in range(1, 11):
    print(f"F({i}) = {nth_fibonacci(i)}")

print(f"First 10: {fibonacci_sequence(10)}")
