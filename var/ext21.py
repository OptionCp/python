def add(a, b):
    print(f"ADDING {a}+{b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a}-{b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b

print("Let's do some math with just functions")

age = add(30, 5)
height = subtract(5, 2)
weight = multiply(40, 2)
iq = divide(100, 2)

print(f"Age:{age}, height:{height}, weight:{weight}, iq:{iq}")
