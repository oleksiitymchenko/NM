import numpy as np
import  math
import matplotlib.pyplot as plt
def Function(x):
    return  x*math.sin(x)

#два массива со значениеми икс и игрек
#x = np.array([0, math.pi/6, 2*math.pi/6, 3*math.pi/6], dtype=float)
x = np.array([0, math.pi/6, 5*math.pi/12, math.pi/2], dtype=float)
y = []
for num in x:
    y.append(Function(num))
y = np.asarray(y,dtype='float')



def lagranz( x, y, t ):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            #пропускаем итый базисный полином
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                #считаем базисный полином
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z

def absolute(tochka):
    return abs(Function(x)-lagranz(x,y,tochka))

print(absolute(math.pi/4))
xnew = np.linspace(np.min(x), np.max(x), 10)
ynew = [lagranz(x, y, i) for i in xnew]

plt.plot(x, y, 'o', xnew, ynew)
plt.grid(True)
plt.show()