import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
        tur.pd()
        tur.setheading(0)
        tur.right(90)
        tur.forward(60)
        tur.left(90)
        tur.forward(40)
        tur.left(90)
        tur.forward(30)
        tur.left(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(30)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(30)
        tur.pu()
        tur.left(180)
        tur.forward(30)
        tur.right(90)
        tur.forward(20)
    elif letter == "C":
        tur.pd()
        tur.setheading(0)
        tur.forward(40)
        tur.right(45)
        tur.forward(15)
        tur.pu()
        tur.right(45)
        tur.fd(40)
        tur.pd()
        tur.right(45)
        tur.fd(15)
        tur.right(45)
        tur.fd(40)
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.pu()
        tur.forward(60)
    elif letter == "D":
        tur.pd()
        tur.setheading(0)
        tur.fd(40)
        tur.right(45)
        tur.fd(15)
        tur.right(45)
        tur.fd(50)
        tur.right(45)
        tur.fd(15)
        tur.right(45)
        tur.fd(40)
        tur.right(90)
        tur.fd(70)
        tur.right(90)
        tur.pu()
        tur.fd(60)
    elif letter == "E":
        tur.pd()
        tur.setheading(0)
        tur.right(90)
        tur.fd(60)
        tur.left(90)
        tur.fd(40)
        tur.left(180)
        tur.fd(40)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(40)
        tur.pu()
        tur.fd(20)
    elif letter == "F":
        tur.pd()
        tur.setheading(0)
        tur.right(90)
        tur.fd(60)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(40)
        tur.pu()
        tur.fd(10)
    elif letter == "G":
        tur.pd()
        tur.setheading(0)
        tur.fd(40)
        tur.right(90)
        tur.fd(20)
        tur.left(180)
        tur.fd(20)
        tur.left(90)
        tur.fd(40)
        tur.left(90)
        tur.fd(60)
        tur.left(90)
        tur.fd(40)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(10)
        tur.pu()
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(65)
        tur.right(90)			
    elif letter == "H":
        tur.pendown()
        tur.right(90)
        tur.forward(40)
        tur.backward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.backward(40)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.left(90)
        tur.forward(20)
        tur.right(90)
        tur.penup()
        tur.forward(40)
    elif letter == "I":
        tur.pendown()
        tur.setheading(0)
        tur.right(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(20)
        tur.backward(40)
        tur.forward(20)
        tur.left(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(20)
        tur.backward(40)
        tur.right(180)
        tur.penup()
        tur.fd(50)
    elif letter == "J":
        tur.pendown()
        tur.backward(40)
        tur.forward(20)
        tur.right(90)
        tur.forward(40)
        tur.circle(-20,180)
        tur.penup()
        tur.circle(20,180)
        tur.left(90)
        tur.forward(84)
        tur.left(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(30)
        tur.penup()
    elif letter == "K":
        tur.pendown()
        tur.right(90)
        tur.forward(50)
        tur.backward(20)
        tur.left(50)
        tur.forward(30)
        tur.backward(30)
        tur.left(80)
        tur.forward(30)
        tur.backward(30)
        tur.left(10)
        tur.penup()
        tur.forward(40)
        tur.right(45)
        tur.forward(10)
        tur.penup()
    elif letter == "L":
        tur.pendown()
        tur.right(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(40)
        tur.backward(40)
        tur.left(90)
        tur.penup()
        tur.forward(60)
        tur.right(90)
        tur.forward(30)
        tur.penup()
    elif letter == "M":
        tur.pendown()
        tur.right(90)
        tur.forward(40)
        tur.backward(40)
        tur.left(45)
        tur.forward(40)
        tur.left(90)
        tur.forward(40)
        tur.right(135)
        tur.forward(40)
        tur.penup()
        tur.backward(40)
        tur.left(90)
        tur.forward(10)
    elif letter == "N":
        tur.pendown()
        tur.right(90)
        tur.forward(40)
        tur.backward(40)
        tur.left(45)
        tur.forward(50)
        tur.left(140)
        tur.forward(40)
        tur.penup()
        tur.right(90)
        tur.forward(10)
    elif letter == "O":
        tur.penup()
        tur.fd(30)
        tur.right(90)
        tur.fd(50)
        tur.left(90)
        tur.pendown()
        tur.circle(30,360)
        tur.penup()
        tur.circle(30,110)
        tur.right(90)
        tur.forward(20)
    elif letter == "P":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(40)
        tur.right(180)
        tur.fd(40)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(65)					
    elif letter == "Q":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.left(45)
        tur.fd(10)
        tur.right(180)
        tur.fd(20)
        tur.pu()
        tur.right(180)
        tur.fd(10)
        tur.left(135)
        tur.fd(30)
        tur.right(90)
        tur.fd(10)
    elif letter == "R":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(40)
        tur.right(180)
        tur.fd(40)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.left(135)
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.fd(30)
        tur.right(135)
        tur.fd(20)
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(10)
    elif letter == "S":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.fd(5)
        tur.pd()
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(30)
    elif letter == "T":
        tur.setheading(0)
        tur.pu()
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(40)
        tur.right(180)
        tur.fd(40)
        tur.left(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(40)
        tur.pu()
        tur.fd(5)
    elif letter == "U":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.pd()
        tur.fd(40)
        tur.left(45)
        tur.fd(10)
        tur.left(45)
        tur.fd(10)
        tur.left(45)
        tur.fd(10)
        tur.left(45)
        tur.fd(40)
        tur.pu()
        tur.right(90)
        tur.fd(10)
    elif letter == "V":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.pd()
        tur.right(65)
        tur.fd(40)
        tur.left(130)
        tur.fd(40)
        tur.pu()
        tur.right(65)
        tur.fd(10)
    elif letter == "W":
        tur.pendown()
        tur.right(90)
        tur.forward(30)
        tur.left(130)
        tur.forward(30)
        tur.right(90)
        tur.forward(30)
        tur.left(135)
        tur.forward(30)
        tur.right(90)
        tur.penup()
        tur.forward(10)
    elif letter == "X":
        tur.pendown()
        tur.right(50)
        tur.forward(40)
        tur.left(180)
        tur.forward(30)
        tur.left(85)
        tur.forward(30)
        tur.right(180)
        tur.forward(40)
        tur.right(30)
    elif letter == "Y":
        tur.pendown()
        tur.right(50)
        tur.forward(40)
        tur.left(90)
        tur.forward(40)
        tur.right(180)
        tur.forward(40)
        tur.left(50)
        tur.forward(40)
        tur.penup()
        tur.right(180)
        tur.forward(40)
        tur.right(50)
        tur.forward(40)
        tur.right(30)
    elif letter == "Z":
        tur.pendown()
        tur.forward(60)
        tur.right(135)
        tur.forward(60)
        tur.left(135)
        tur.forward(60)
        tur.penup()
        tur.left(90)
        tur.forward(60)
        tur.right(90)		

        
    elif letter == "Ax":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(30)
        tur.pd()
        tur.left(45)
        tur.fd(30)
        tur.left(180)
        tur.fd(15)
        tur.right(90)
        tur.fd(15)
        tur.left(180)
        tur.fd(30)
        tur.pu()
        tur.left(90)
        tur.fd(50)
        tur.right(90)
        tur.left(35)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("O",tur)


    window.exitonclick()

