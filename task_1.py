def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sin(x):
    pi = 3.14159265358979323846
    k = int(x / (2 * pi))
    x = x - k * 2 * pi
    if x > pi:
        x = x - 2 * pi
    
    result = 0
    term = x
    x_squared = x * x
    for n in range(20):
        result += term
        term *= -x_squared / ((2 * n + 2) * (2 * n + 3))
    return result


def cos(x):
    pi = 3.14159265358979323846
    k = int(x / (2 * pi))
    x = x - k * 2 * pi
    if x < 0:
        x = -x
    if x > pi:
        x = x - 2 * pi
    
    result = 0
    term = 1
    x_squared = x * x
    for n in range(20):
        result += term
        term *= -x_squared / ((2 * n + 1) * (2 * n + 2))
    return result


def exp(x):
    result = 1.0
    term = 1.0
    n = 1
    while True:
        term *= x / n
        prev = result
        result += term
        if abs(result - prev) < 1e-15 or n >= 100:
            break
        n += 1
    return result
