import random

start = 0
end = 10
accuracy = 1e-04

def func(x):
    return((2+5*pow(x,3))**(1/6))


def SimpleIter(f, start, end, accuracy):
    x = random.randrange(start,end)
    while abs(x - f(x))>accuracy:
        x=f(x)
    return round(x,4)


print("answer is",SimpleIter(func,start,end,accuracy))
