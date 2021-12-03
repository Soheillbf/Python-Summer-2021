ls=[]
n=int(input("please enter an integer number"))
isPrime=True
for i in range(2,n//2):
    if n%i==0:
        isPrime=false
if isPrime and n!=0:
    print("The entered number is prime")
else:
    print("The entered number is not prime")






##count=0
##ls=[]
##n=int(input("please enter an integer number"))
##for i in range(2,n//2):
##    if n%i==0:
##        count+=1
##    ls.append(count)
##if count>=2:
##    print("The entered number is not prime")
##else:
##    print("The entered number is prime")
##
##print(ls)









##import math
##math.factorial 
##
##n=int(input("Please enter an integet number as the rows"))
##
##for i in range(n):
##    print(" "*(n-i), end="")
##
##    print(" " .join(map(str, str(11**i))))
##    
##
##

##from math import factorial
##n=5
##for i in range(n):
##    for j in range(n-i+1):
##        print(end=" ")
##    for j in range(i+1):
##        print(factorial(i)//factorial(j)*factorial(i-j)), end=" ")
##    print()
##
##



"""--------------------------Lozenge shape------------------------------"""
##n=int(input("please enter an integer number"))
##for i in range(1,n+1):
##    print(" "* (n-i+1) , end="")
##    for j in range(i):
##        print("* " , end="")
##    print()
##
##for i in range(n+1,n-i,-1):
##    print(" "* (n-i+1), end="")
##    for j in range(i):
##        print("* " , end="")
##    print()
"""------------------------------Triangle-------------------------------"""
##n=int(input("please enter an integer number"))
##for i in range(1,n+1):
##    for j in range(i):
##        print("* " , end="")
##    print()
##
##for i in range(n+1,n-i,-1):
##    for j in range(i):
##        print("* " , end="")
##    print()

"""-------------------------------Square-------------------------------"""
##n=int(input("please enter an integer number"))
##for i in range(n):
##    for j in range(n):
##        if i==0 or j==0 or i==n-1 or j==n-1:
##            print("* ",end="")
##        else:
##            print("  ", end="")
##    print(" ")
##
"""----square 2-----"""
##x=int(input("please enter an integer number"))
##for i in range(x,x-1,-1):
##    print("* "* x, end='')
##    print()
##
##for i in range(x-1,x-i+1,-1):
##    print("*" , end=" "*x,)
##    print()
##
##for i in range(x-x+1,0,-1):
##    print("* "* x, end='')
##    print()
















"""-------------------------------Fibonacci-------------------------------------------------"""
##n=int(input("please enter an integer number"))
##
##m=int(input("please enter an integer number"))
##if 90<m<100:
##    print(Fibonacci(n),Fibonacci(n-1),Fibonacci(n-2),Fibonacci(n-3),Fibonacci(n-4),Fibonacci(n-5),Fibonacci(n-6),Fibonacci(n-7),Fibonacci(n-8))
##    
##
##def Fibonacci(n):
##    if n<0:
##        print("incorrect number is entered")
##    elif n==1:
##        return 0
##    elif n==2:
##        return 1
##    else:
##        return Fibonacci(n-1)+Fibonacci(n-2)
##print(Fibonacci(n),Fibonacci(n-1),Fibonacci(n-2),Fibonacci(n-3),Fibonacci(n-4),Fibonacci(n-5),Fibonacci(n-6),Fibonacci(n-7),Fibonacci(n-8))
##fiboNumber=[Fibonacci(20)]    
##
##



"""-----------------------------Reverse---------------------------------------------"""
##count=0
##n=int(input("please enter an integer number"))
##while n:
##    count=count*10+ n%10
##    n//=10
##print(count)
"""--------------------------------------------------------------------------"""
##count=0
##n=int(input("please enter an integer number"))
##while n:
##    n//=10
##    count+=1
##print(count)
"""----------------------------Length---------------------------------------------"""
##x=int(input("please enter an integer number"))
##d=len(str(x))
##print(d)
"""--------------------------------------------------------------------"""
