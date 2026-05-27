# Functions and Scope
global_var = "I'm global"

def greet(name, greeting="Hello"):
    local_var = f"{greeting}, {name}!"
    print(local_var)
    print(global_var)

def square(n):
    return n * n

greet("Camper")
print(square(5))
