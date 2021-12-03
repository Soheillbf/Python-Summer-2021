class Quadratic:
    def __init__(self,a=0,b=0,c=0):
        self.a=a
        self.b=b
        self.c=c
        self.__a=0
        self.__b=0
        self.__c=0
    def ans(self,delta):
        self.delta=(self.b**2)-(4*self.a*self.c)
        if self.delta>0:
            from math import sqrt
            return f'The first answer equals (X1)={(-self.b+(sqrt(self.delta)))/2*self.a}\nThe second answer equals(X2)={(-self.b-(sqrt(self.delta)))/2*self.a}'
        elif self.delta==0:
            return f'-+{(self.b)/2*self.a}'
        else:
            print("The equation has no real answer")
    @property
    def delta(self):
        return self.__delta
    @delta.setter
    def delta(self,delta):
        if isinstance(delta,int):
            self.__delta=delta
        else:
            print("Error!")
    def __str__(self):
        return f'{self.ans(q)}'
    def __repr__(self):
        return f'We have solved the quadratic equation in terms of {self.a}X^2+{self.b}X+{self.c}'
if __name__=="__main__":
    q=Quadratic(1,7,6)
    print(q)

