import math
import matplotlib.pyplot as plt
def factorial(n):
    if not n:
        return 1
    else:
        return n*factorial(n-1)
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
## An other way to code Fibonacci series
def fibo_2(n):
    if n==1 or n==2:
        return 1
    f=[1,1]
    for i in range(3,n+1):
        f.append(sum(f[-2:]))
    return f[-1]

def draw_fib(n):
    x=[]
    y=[]
    x=[i for i in range(1,n)]
    y=[fibo_2(i) for i in x]
    plt.plot(x,y,"rD")
    plt.show() 
##Estimate the Golden Rarion of Fibonacci series
def Golden_ratio(n):
    if n==2:
        return 1
    elif n==3:
        return 2
    elif n==4:
        return 3/2
    else:
        return fibo_2(n)/fibo_2(n-1)
def draw_Golden_ratio(n):
    x=[]
    y=[]
    x=[i for i in range(1,n)]
    y=[Golden_ratio(i) for i in x]
    plt.plot(x,y)
    plt.show()
    
"""Sin and Cos functions(Bazgashti)"""
##def cos(x,n=18):
##    if not n:
##        return 1
##    else:
##        return (-1)**n * x**2*n /factorial(2*n) + cos(x,n-1)
##def sin(x,n=18):
##    if not n:
##        return 1
##    else:
##        return (-1)**n * x**2*n+1 /factorial(2*n+1) + sin(x,n-1)
def sin(x,n=10):
    r=0
    for i in range(n+1):
        temp=2*i+1
        r+= (-1)**i * x**temp/factorial(temp)
    return r

def cos(x,n=10):
    r=0
    for i in range(n+1):
        temp=2*i
        r+= (-1)**i * x**temp/factorial(temp)
        
def deg2rad(deg):
    import math
    return math.pi*deg/180
    
    
def neper(x,n):
    if not n:
        return 1
    else:
        return x**n/factorial(n) + neper(x,n-1)
def inc(x):
    return x+1
def dec(x):
    return x-1
def add(a,b):
    if not b:
        return a
    else:
        return add(inc(a),dec(b))



if __name__=="__main__":
##    n=int(input("n= "))
##    draw_Golden_ratio(n)

    
 
##    import math
##    x=[]
##    y=[]
##    z=[]
##    x=[i for i in range(0,361)]
##    y=[sin(deg2rad(i)) for i in x]
##    z=[cos(deg2rad(i)) for i in x]
##    plt.plot(x,y)
##    plt.plot(x,z)
##    plt.show()
##    for i,j in zip(x,y):
##        print(i,j)
##    





