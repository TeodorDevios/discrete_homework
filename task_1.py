def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sin(x):
    pi = 3.14159265358979323846
    while x > pi:
        x -= 2 * pi
    while x < -pi:
        x += 2 * pi
    result = 0
    for n in range(20):
        sign = (-1) ** n
        numerator = x ** (2 * n + 1)
        denominator = factorial(2 * n + 1)
        result += sign * numerator / denominator
    return result


def cos(x):
    pi = 3.14159265358979323846
    while x > pi:
        x -= 2 * pi
    while x < -pi:
        x += 2 * pi
    result = 0
    for n in range(20):
        sign = (-1) ** n
        numerator = x ** (2 * n)
        denominator = factorial(2 * n)
        result += sign * numerator / denominator
    return result


def exp(x):
    result = 0
    for n in range(30):
        numerator = x ** n
        denominator = factorial(n)
        result += numerator / denominator
    return result


if __name__ == '__main__':
    print(sin(113))
    print(cos(113))
    print(exp(113))