import  math
startpoint = 1
endpoint = 5
accuracy = 1e-3

def func(x):
    return math.sqrt(9+math.pow(x,2))

def RectangleMethod(startpoint, endpoint, accuracy, f):
    sum = 0
    while(startpoint<endpoint-accuracy):
        startpoint+=accuracy
        sum+=f(startpoint)*accuracy
    return round(sum,3)

print(RectangleMethod(startpoint,endpoint,accuracy,func))