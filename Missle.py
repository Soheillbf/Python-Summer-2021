class missle:
    def __init__(self,Mmass,Fmass,v,v_rel,rate,g):
        self.Mmass=Mmass
        self.Fmass=Fmass
        self.v=v
        self.v_rel=v_rel
        self.rate=rate
        self.g=9.80665
    def height(self):
        import math
        from math import log
        self.h= (-0.5*self.g) * ((self.Fmass) / (self.rate))**2 + (self.v_rel / self.rate)*(self.Fmass - self.Mmass * math.log(1+(self.Fmass / self.Mmass)))
        return self.h
##    def __str__(self):
##        x=f'{self.h}'
##        return x
H=missle(10000,100,1,-50,2,"self.g")
print(H)
print(missle.height(H))

