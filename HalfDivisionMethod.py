start = 0
end = 10
accuracy = 1e-04

average = lambda a, b: (a + b) / 2

#функция
def func( x ):
    return pow(x, 6) - 5 * pow(x, 3) - 2

#погрешность
def IsSatisfy( x, y ):
    if abs(x - y) <= accuracy:
        return True
    else:
        return False

#знаки функции в 2-х точках должны быть равны
def CheckEndings( f, startpoint, endpoint ):
    if f(startpoint) * f(endpoint) <= 0:
        return True
    return False


def HalfDivision( f, start, end ):
    if not CheckEndings(f, start, end): return "Incorrect endings"

    middle = average(start, end)
    if IsSatisfy(start, end): return middle

    if CheckEndings(func, start, middle):
        middle = HalfDivision(f, start, middle)
    else:
        middle = HalfDivision(f, middle, end)

    return round(middle, 4)


print(HalfDivision(func, start, end))
