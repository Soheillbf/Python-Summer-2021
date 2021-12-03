import time
import turtle
pen=turtle.Turtle()
pen.speed(-1)
turtle.bgcolor("black")

hour=int(time.strftime("%I"))
minute=int(time.strftime("%M"))
second=int(time.strftime("%S"))

def draw_clock(hour,minute,second,pen):
    pen.up()
    pen.goto(0,260)
    pen.setheading(180)
    pen.down()
    pen.color("gray")
    pen.circle(260)

    pen.up()
    pen.goto(0,0)
    pen.setheading(90)
    
    for i in range(12):
        pen.fd(240)
        pen.down()
        pen.fd(20)
        pen.up()
        pen.goto(0,0)
        pen.right(30)

    pen.up()
    pen.goto(0,0)
    pen.setheading(90)
    
    for i in range(60):
        pen.fd(255)
        pen.down()
        pen.fd(5)
        pen.up()
        pen.goto(0,0)
        pen.right(6)

    pen.up()
    pen.goto(0,0)
    pen.setheading(90)
    pen.color('gray')
    angle=((hour/12)*360)+ (minute*.5)
    pen.right(angle)
    pen.down()
    pen.fd(100)

    pen.up()
    pen.goto(0,0)
    pen.color('gray')
    pen.setheading(90)
    angle=(minute/60)*360
    pen.rt(angle)
    pen.down()
    pen.fd(200)

    pen.up()
    pen.goto(0,0)
    pen.color('gray')
    pen.setheading(90)
    angle=(second/60)*360
    pen.rt(angle)
    pen.down()
    pen.fd(250)

if __name__=="__main__":
    draw_clock(hour,minute,second,pen)


