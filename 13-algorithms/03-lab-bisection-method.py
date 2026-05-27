# Lab: Implement the Bisection Method
def square_root(n, tolerance=0.0001):
    if n < 0:
        raise ValueError("Cannot compute square root of negative number")
    low, high = 0, max(1, n)
    while (high - low) > tolerance:
        mid = (low + high) / 2
        if mid * mid < n:
            low = mid
        else:
            high = mid
    return (low + high) / 2

def bisection(f, a, b, tolerance=0.0001):
    if f(a) * f(b) >= 0:
        raise ValueError("Function must have opposite signs at endpoints")
    while (b - a) > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

print(f"sqrt(25) = {square_root(25):.4f}")
print(f"sqrt(2) = {square_root(2):.4f}")
