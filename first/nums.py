def plus(a, b):
    """ 34343455454"""
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def dev(a, b):
    return a / b


def oct(a, b):
    return a % b


def fin(a, b, c):
    return (plus(a, b) * oct(a, b) + c)


if __name__ == '__main__':
    print(plus(2, 2))
    print(minus(4, 2))
    print(mult(3, 3))
    print(dev(100, 4))
    print(oct(15, 4))
    print(100, 7, 25)
