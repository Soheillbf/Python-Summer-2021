def gcd_(x,y):
    if not y:
        return x
    else:
        return gcd_(y,x%y)

