def addiere(a, b):
    return a + b


def subtrahiere(a, b):
    return a - b


def multipliziere(a, b):
    return a * b


def dividiere(a, b):
    if b == 0:
        raise ValueError("Division durch 0 nicht erlaubt")

    return a / b


if __name__ == "__main__":
    print("Einfacher Calculator")
    print(addiere(5, 3))