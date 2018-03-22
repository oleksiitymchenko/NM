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

average = lambda x,y:(x+y)/2

def TrapezeMethod(startpoint,endpoint,accuracy,f):
    sum=0
    while(startpoint<=endpoint):
        sum+=(f(startpoint)+f(startpoint+accuracy))*accuracy/2
        startpoint+=accuracy
    return round(sum,3)


print("Rectangle: ",RectangleMethod(startpoint,endpoint,accuracy,func))
print("Trapeze: ",TrapezeMethod(startpoint,endpoint,accuracy,func))
