class vector:
    def __init__(self,xaxis,yaxis,R1,x2axis,y2axis,R2,x3axis,y3axis,z3axis,R3):
        from math import sqrt
        self.xaxis=xaxis
        self.yaxis=yaxis
        self.x2axis=x2axis
        self.y2axis=y2axis
        self.x3axis=x3axis
        self.y3axis=y3axis
        self.z3axis=z3axis
        self.R1=abs(sqrt(self.xaxis**2 + self.yaxis**2))
        self.R2=abs(sqrt(self.x2axis**2 + self.y2axis**2))
        self.R3=abs(sqrt(self.x3axis**2 + self.y3axis**2 + self.z3axis**2))
    def getxaxis(self):
        return self.__xaxis
    def setxasix(self,xaxis):
        if isinstance(xaxis, int):
            self.__xaxis=xaxis
        else:
            print("Error")
    xaxis=property(getxaxis,setxasix)
    def getzaxis(self):
        return self.__zaxis
    def setzasix(self,zaxis):
        if isinstance(zaxis, int):
            self.__zaxis=zaxis
        else:
            print("Error")
    zaxis=property(getzaxis,setzasix)

    def __str__(self):
        x=f'{self.xaxis}'
        y=f'{self.yaxis}'
        r=f'{self.R1}'
        x2=f'{self.x2axis}'
        y2=f'{self.y2axis}'
        r2=f'{self.R2}'
        x3=f'{self.xaxis}'
        y3=f'{self.yaxis}'
        z3=f'{self.yaxis}'
        r3=f'{self.R3}'
        return "1)The first coordinatior " + "("+ x + ","+ y+")"+"\t" +"The magnitude |R|="+r +"\n"+"2)The second coordinatior " + "("+ x2 + ","+ y2+")"+"\t" +"The magnitude |R|="+r2 +"\n"+"3)The third coordinatior " + "("+ x3 + ","+ y3+","+z3+")"+"\t" +"The magnitude |R|="+r3 
    def __repr__(self):
        x1=f'{self.xaxis}i'
        y1=f'{self.yaxis}j'
        x2=f'{self.x2axis}i'
        y2=f'{self.y2axis}j'
        x3=f'{self.x3axis}i'
        y3=f'{self.y3axis}j'
        z3=f'{self.z3axis}k'
        return x1 +"+"+ y1+"\n"+x2 +"+"+ y2+"\n"+x3 +"+"+ y3 +"+"+z3
    def compre(self):
        if self.R1>self.R2:
            print("The first vector is bigger")
        elif self.R1==self.R2:
            print("The vectors are equal")
        else:
            print("The second vector is bigger")
    def sum_x(self):
        self.I=self.xaxis+self.x2axis
        return self.I
    def sum_y(self):
        self.J=self.yaxis+self.y2axis
        return self.J
    def multi_x(self):
        self.I1=self.xaxis*self.x2axis
        return self.I1
    def multi_y(self):
        self.J1=self.yaxis*self.y2axis
        return self.J1
    def angle(self):
        from math import acos
        def rad2degree(n):
            return n*57.296
        return rad2degree(acos(self.multi_x()+self.multi_y()/self.R1*self.R2))
##if __name__=="__main__":
##    bordar=vector(0,5,"self.R1",5,0,"self.R2")
##    print(f"{bordar}")
##    print(f"3)Sum of the vectors= {vector.sum_x(bordar)}i + {vector.sum_y(bordar)}j")
##    print(f"4)Dot product of the vectors= {vector.multi_x(bordar)}i + {vector.multi_y(bordar)}j")
##    print(f"5)The angle between the vectors= {vector.angle(bordar)} degrees") 
##    print(f"{vector.compre(bordar)}")
##from vector import vector
##class vector3(vector):
##    def __init__(self,xaxis=0,yaxis=0,zaxis=0,R3):
##        vector.__init__(self,xaxis,yaxis)
##        self.__zaxis=0
##        self.zaxis=zaxis
##        self.R3=abs(sqrt(self.x2axis**2 + self.y2axis**2))
##    def getzaxis(self):
##        return self.__zaxis
##    def setzasix(self,zaxis):
##        if isinstance(zaxis, int):
##            self.__zaxis=zaxis
##        else:
##            print("Error")
##    zaxis=property(getzaxis,setzasix)
##    def __str__(self):
        
if __name__=="__main__":
    bordar=vector(0,5,"self.R1",5,0,"self.R2",5,0,3,"self.R3")
    print(f"{bordar}")
##    print(f"3)Sum of the vectors= {vector.sum_x(bordar)}i + {vector.sum_y(bordar)}j")
##    print(f"4)Dot product of the vectors= {vector.multi_x(bordar)}i + {vector.multi_y(bordar)}j")
##    print(f"5)The angle between the vectors= {vector.angle(bordar)} degrees") 
##    print(f"{vector.compre(bordar)}")





























    

class fraction_:
    def __init__(self,numer,denomer,numer2,denomer2,reduce1,reduce2,reduce3,reduce4):
        from math import gcd
        self.numer=numer
        self.denomer=denomer
        self.reduce1=self.numer/gcd(self.numer,self.denomer)
        self.reduce2=self.denomer/gcd(self.numer,self.denomer)
        self.numer2=numer2
        self.denomer2=denomer2
        self.reduce3=self.numer2/gcd(self.numer2,self.denomer2)
        self.reduce4=self.denomer2/gcd(self.numer2,self.denomer2)
    def sum_frac(self):
        self.s_s=(self.reduce1*self.reduce4)+(self.reduce2*self.reduce3)/self.reduce2*self.reduce4
        return self.s_s
    def __str__(self):
        x=f'{self.numer}'
        y=f'{self.denomer}'
        r=f'{self.reduce1}'
        r2=f'{self.reduce2}'
        x2=f'{self.numer2}'
        y2=f'{self.denomer2}'
        r3=f'{self.reduce3}'
        r4=f'{self.reduce4}'
        return x+ "/" +y +"  The reduce fraction= "+ r+"/"+r2 +"\n"+ x2+ "/" +y2 +"  The reduce fraction= "+ r3+"/"+r4      
if __name__=="__main__":
    kasr=fraction_(15,25,20,24,"self.reduce1","self.reduce2","self.reduce3","self.reduce4")
    print(kasr)




















