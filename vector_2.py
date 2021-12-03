class vector:
    def __init__(self,x=0,y=0):
        self.__x=0
        self.__y=0
        self.x=x
        self.y=y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,x):
        if isinstance(x,int):
            self.__x=x
        else:
            print("Error")
##    @property
##    def y(self):
##        return self.__y
##    @x.setter
##    def y(self,x):
##        if isinstance(y,int):
##            self.__y=y
##        else:
##            print("Error")
    def gety(self):
        return self.__y
    def sety(self,y):
        if isinstance(y,int):
            self.__y=y
        else:
            print("Error")
    y=property(gety,sety)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    def __mul__(self,w):
        return self.x*w.x+self.y*w.y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f'{self.x:+}i{self.y:+}j'
    def __add__(self,w):
        return vector(self.x+w.x,self.y+w.y)
    
    
if __name__=="__main__":
    v=vector(2,3)
    u=vector(3,-4)
    print(f"v ={v}")
    print(f"u ={u}")
    print(f"|u| ={abs(u)}")
    print(f"v*u ={v*u}")
    print(f"v+u ={v+u}")



    
    
