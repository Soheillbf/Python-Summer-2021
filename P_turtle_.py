import turtle
pen=turtle.Turtle()
pen.speed(-1)
def polygun(n,size=100):
    angle=360/n
    for i in range(n):
        pen.fd(size)
        pen.left(angle)
def goto(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()
def polygun_2(n,size,x=0,y=0,color='yellow'):
    pen.color(color)
    goto(x,y)
    pen.begin_fill()
    polygun(n,size)
    pen.end_fill()

def draw(n,colors=['red','green','blue','yellow','black']):
    for i in range(3,n):
        pen.color(colors[i%5])
        polygun_2(i)
        goto(-i*50,-i*50)
def spiral(n):
    for i in range(n):
        pen.color(i/n,i/n,i/n)
        pen.fd(i)
        pen.left(90)

def shape(n):
    turtle.bgcolor('black')
    for i in range(n):
        pen.color(i/n,i/n,i/n)
        pen.fd(i)
        pen.left(69)

def star():
    import random
    turtle.bgcolor('darkblue')
    t=random.randrange(256)
    m=random.randrange(100)
    rang=f"#{t:02x}{t:02x}00"
    sz=random.randrange(1,5)
    x1=random.randrange(-200,200)
    y1=random.randrange(-200,150)
    polygun_2(n=30,size=sz,x=x1,y=y1,color=rang)
def shab(n):
    for i in range(n):
        star()
def sun_flower(n):
    turtle.bgcolor('black')
    colors=['red','orange','green','yellow','blue','skyblue']
    for i in range(1,n):
        pen.color(colors[i%6])
        pen.circle(i,20)
    
shab(100)  
