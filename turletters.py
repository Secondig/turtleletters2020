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
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
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
        tur.forward(10)
    elif letter == "I":
	tur.pendown()
        tur.setheading(0)
        tur.right(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(40)
        tur.backward(80)
        tur.forward(40)
        tur.left(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(40)
        tur.backward(80)
        tur.right(180)
        tur.penup()
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
        tur.forward(20)
        tur.penup()
    elif letter == "K":
	tur.pendown()
        tur.left(90)
        tur.forward(50)
        tur.backward(20)
        tur.right(50)
        tur.forward(30)
        tur.backward(30)
        tur.right(80)
        tur.forward(30)
        tur.backward(30)
        tur.left(80)
        tur.penup()
        tur.forward(50)
        tur.right(45)
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
        tur.forward(5)
    elif letter == "O":
	tur.pendown()
        tur.circle(40,360)
        tur.penup()
        tur.circle(40,110)
        tur.right(90)
        tur.forward(20)
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
