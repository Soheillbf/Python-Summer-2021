##def pascalTriangle(n):
##    trow=[1]
##    y=[0]
##    for x in range(n):
##        print(trow)
##        trow=[left+right for left,right in zip(trow+y , y+trow)]


##from math import factorial
##
##n=int(input("Please enter an integet number as the rows"))
##
##for i in range(n):
##    for j in range(n-i+1):
##        print(end=" ")
##    for j in range(i+1):
##        print(factorial(i)//factorial(j)*factorial(i-j), end=" ")
##
##    print()
