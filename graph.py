import threading

def print_odd(n):
    for i in range(1,n+1,2):
        print(i)

def print_even(n):
    for i in range(0,n+1,2):
        print(i)
##if __name__=="__main__":
##    t1=threading.Thread(target=print_odd,args=(100,))
##    t2=threading.Thread(target=print_even,args=(100,))
##    t1.start()
##    t2.start()
##    t1.juin()
##    t2.juin()
##    print("Good bye")
def path(n,m,way):
    if n==0 or m==0:
        print(way)
        return
    if n:
        way1=way[:]
        way1+="^"
        path(n-1,m,way1)
    
    if m:
        way2=way[:]
        way2+=" ->"
        path(n,m-1,way2)
if __name__=="__main__":
    t1=threading.Thread(target=path,args(3,2,""))
    
