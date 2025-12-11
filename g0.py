def add(a, b):
    return a + b

def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result = add(result, a)
    return result

def main():
    x = add(1, 2)
    y = multiply(3, 4)
    return x + y