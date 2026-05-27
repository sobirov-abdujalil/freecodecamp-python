# Understanding Error Handling
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input type"
    else:
        return f"Result: {result}"
    finally:
        print("Division attempted")

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "a"))
