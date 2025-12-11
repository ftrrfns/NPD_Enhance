def add(a, b):
    return a + b

def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result = add(result, a)
    return result

def preprocess(a):
    return add(a, 1)

def main():
    x = add(1, 2)
    t = preprocess(3)
    y = multiply(t, 4)
    return x + y