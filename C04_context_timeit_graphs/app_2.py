import timeit
import time

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return result

def factorial2(n):
    if n<=1:
        return 1
    else:
        return n*factorial2(n-1)

def timing():
    a=[]
    b=[]
    for i in range(1,999):
        y=time.time()
        factorial(i)
        z=time.time()
        a.append(z-y)
    for i in range(1,999):
        y=time.time()
        factorial(i)
        z=time.time()
        b.append(z-y)
    return a,b

if __name__ == "__main__":
    print(timing())

    #factorial(3)
    #x=timeit.timeit('factorial(3)')
    #print(x)