def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    if b < 0:
        return subtract(a, b)
    else:
        return add(a, b)

def main():
    x = add(1, 2)
    y = multiply(3, 4)
    return x + y