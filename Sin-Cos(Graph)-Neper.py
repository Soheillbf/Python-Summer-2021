import matplotlib.pyplot as plt
##from math import factorial
def fibo(n):
    if n==1 or n==2:
        return 1
    f=[1, 1]
    for i in range(3,n+1):
        f.append(sum(f[-2:]))
    return f[-1]
def sin(x,n):
    r=0
    for i in range(n+1):
        temp=2*i+1
        r+= (-1)**i * x**temp/factorial(temp)
    return r
def cos(x,n):
    r=0
    for i in range(n+1):
        temp=2*i
        r+= (-1)**i * x**temp/factorial(temp)
    return r
def draw_fib(n):
    x=[]
    x=[i for i in range(1,n+1)]
    y=[]
    y=[fibo(i) for i in x]
    plt.plot(x,y)
    plt.show()
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def deg2rad(x):
    import math
    return math.pi*deg2rad/180
##if __name__=="__main__":
##    print(factorial(5))
if __name__=="__main__":
    import math
    x=[]
    x=[i for i in range(0,361)]
    y=[]
    y=[sin(i) for i in range(x)]
    z=[cos(i) for i in range(x)]

    plt.plot(x,y)
    plt.plot(x,z,'cD')
    plt.show()

"""----------------------------------------Fibonacci series-----------------------------"""
"""return function"""


##def fibo(n):
##    if n==1 or n==2:
##        return 1
##    f=[1, 1]
##    for i in range(3,n+1):
##        f.append(sum(f[-2:]))
##    return f[-1]
##if __name__=="__main__":
##    print(fibo(10))
##                
"""-----------------------------------Print the prime numbers-------------------------"""
##n=int(input("Please enter the maximum number= "))
##m=int(input("Please enter the minimum number= "))
##count=0
##ls=[]
##for i in range(m,n+1):
##    for j in range(1,i):
##        if i%j==0:
##            count+=1
##    if count<3:
##        ls.append(i)
##
##print(ls)
"""------------------------------------Sum of the digits-----------------------"""
##n=int(input("Please enter an integer number= "))
##s=0
##for i in range(n):
##    s=s+n%10
##    n=n//10
##print(f"sum of the digits is {s}")
"""-------------------------------------Taylor e^x----------------------------"""
##from math import factorial
##s=0
##x=int(input("Please enter an integer number= "))
##for i in range(0,1000):
##    
##    s=s+ (x**i)/factorial(i)
##
##print(f"{s}")
"""---------------------------------------Complete number-----------------------"""
##n=int(input("Please enter the power"))
##ls=[]
##for i in range(2,n):
##    if not n%i:
##        ls.append(i)
##if sum(ls)==n:
##    print(f"The entered number ({n}) is complete number")
##else:
##    print(f"The entered number ({n}) is not complete number")
"""--------------------------------------Factorial---------------------"""
##n=int(input("Please enter the power"))
##p=1
##i=1
##s=0
##for i in range(1,n+1):
##    if i>50:
##        break
##    else:
##        p=p*i
##for i in range(1,n+1):
##    s=s+p
##print(f"{n}!={p}")

##def factorial(n):
##    if n==0:
##        return 1
##    else:
##        return n*factorial(n-1)
##
##if __name__=="__main__":
##    factorial(5)
##    
"""------------------------------------------Sum of the factorials-------------------"""
##from math import factorial
##n=int(input("Please enter the power"))
##s=0
##for i in range(1,n+1):
##    s=s + factorial(i)
##print(s)
















##from math import factorial
##sum=1
##for i in range(1,101):
##    sum=sum + (x**i / factorial(i))
##print(sum)









##from math import factorial
##def sum(n):
##    s=0
##    for i in range(50):
##        s=s + (i / factorial(i))
##def function(x):
##    E= sum_(50)* x
##if __name__=="__main__":
##    function(2)















##
##from math import factorial
##x=int(input("Enter an integer number"))
##for i in range():
##    s=0
##    s=s + (x ** i / factorial(i))
##
##print(s)




















##from math import factorial
##def neper(n):
##    n=15
##    for i in range(n):
##        s=0
##        s=s+ 1/factorial(n)
####def neper_functin(x):
####    neper(n) ** x
##
##print(neper(5))
##if __name__=="__main__":
##    neper(5)
    



##from math import factorial
##n=int(input("Enter an integer number"))
##s=0
##for i in range(0,n+1):
##    s= s + 1/factorial(n)
##x=int(input("Enter an integer number (the power) "))
##
##E=s**x
##
##
##print(s)




