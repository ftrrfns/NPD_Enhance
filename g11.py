def add(a, b):
    return a + b

def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result = add(result, a)
    return result

def subtract(a, b):
    return a - b

def safe_multiply(a, b):
    if b < 0:
        return subtract(a, b)
    else:
        return multiply(a, b)

def main():
    x = add(1, 2)
    y = safe_multiply(3, 4)
    return x + y
