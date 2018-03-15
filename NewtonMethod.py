import random

start = 1
end = 5
accuracy = 1e-04
x0 = random.randrange(start, end)


# функция
def func(x):
    return pow(x, 6) - 5 * pow(x, 3) - 2


# производная первого порядка
def derivative_1(x):
    return 6 * pow(x, 5) - 15 * pow(x, 2)


# производная второго порядка
def derivative_2(x):
    return 30 * pow(x, 4) - 30 * x


# проверка на разность знаков концов отрезка
def IsInequality_1(f, a, b):
    if (f(a) * f(b)) < 0:
        return True
    else:
        return False


# проверка условия для применения метода ньютона знак второй производной и функции одинаковый
def IsInequality_2(fF, fDer_2, x0):
    if (fF(x0) * fDer_2(x0)) > 0:
        return True
    else:
        return False


def NewtonMethod(a, b, eps, fF, fDer_1, fDer_2, x):
    #проверки применим ли метод Ньютона
    if not IsInequality_1(fF, a, b): return "Problem with first inequality"
    if not IsInequality_2(fF, fDer_2, x): return "Problem with second inequality"

    # t для первой итерации
    t = fF(x) / fDer_1(x)

    # формула x(k+1)=x(k)-f`(x(k))/f(x(k))
    while (abs(t) > eps):
        t = fF(x) / fDer_1(x)
        x -= t

    return round(x, 4)


print("answer is ", NewtonMethod(start, end, accuracy, func, derivative_1, derivative_2, x0))
