def SUM(x, y):
    return x + y


def MUL(x, y):
    return x * y


def SUB(x, y):
    return x - y


def DIV(x, y):
    return x / y


def PER(x, y):
    return (x * 100) / y


def SAP(x):
    number = []
    oper = []

    a = ''

    for i in x:

        if i.isnumeric():

            a = a + i
        elif i == '.':
            a = a + i
        else:
            number.append(float(a))
            oper.append(i)
            a = ''

    if a != '':
        number.append(float(a))
    return number, oper


def OPER(x, y, z):
    x = float(x)
    z = float(z)
    if y == '+':
        a = SUM(x, z)
        return a
    elif y == '-':
        a = SUB(x, z)
        return a
    elif y == '*':
        a = MUL(x, z)
        return a
    elif y == '/':
        a = DIV(x, z)
        return a
    elif y == '^':
        a = EXP(x, z)
        return a
    elif y == '%':
        a = PER(x, z)
        return a


def EXP(x, y):
    return x ** y


def CAL(n, o):
    a = OPER(n[0], o[0], n[1])
    i = 0
    k = a
    while len(o) > i + 1:
        b = OPER(k, o[i + 1], n[i + 2])
        k = b
        i = i + 1
    return k
