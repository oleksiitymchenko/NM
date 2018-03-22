import  math
#границы интегрирования
startpoint = 1
endpoint = 5
#шаг вычисления
step = 1e-4

#функция
def func(x):
    return math.sqrt(9+math.pow(x,2))

#метод прямоугольников
def RectangleMethod(startpoint, endpoint, accuracy, f):
#сумма площадей прямоугольников
    sum = 0
#вычисления по формуле прямоугольников
    while(startpoint<endpoint-accuracy):
        startpoint+=accuracy
        sum+=f(startpoint)*accuracy
    return round(sum,3)

#метод трапеция
def TrapezeMethod(startpoint,endpoint,accuracy,f):
#сумма площадей трапеции
    sum=0
#вычисления по формуле площади трапеций
    while(startpoint<=endpoint):
        sum+=(f(startpoint)+f(startpoint+accuracy))*accuracy/2
        startpoint+=accuracy
    return round(sum,3)


#метод симсона
def SimpsonMethod(startpoint, endpoint, step, f):
    #сумма значений функции на каждом шагу
    sum = 0
    i = 2
    #цикл с шагом в 2 чтобы высчитать значение для суммы
    #на каждом шагу считаем значение для парного и значение предыдущего непарного
    while i<= (endpoint - startpoint)/step:
        sum+=2*f(startpoint+i*step)
        sum+=4*f(startpoint+(i-1)*step)
        i+=2
    sum = (step/3)*(f(startpoint)+f(endpoint)+sum)
    return round(sum,3)

print("Rectangle: ", RectangleMethod(startpoint, endpoint, step, func))
print("Trapeze: ", TrapezeMethod(startpoint, endpoint, step, func))
print("Simpson", SimpsonMethod(startpoint,endpoint,step,func))
