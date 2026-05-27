# Lab: Build a Number Pattern Generator
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def triangular(n):
    return [i * (i + 1) // 2 for i in range(1, n + 1)]

print("Fibonacci:", fibonacci(10))
print("Triangular:", triangular(10))
