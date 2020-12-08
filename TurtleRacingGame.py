from turtle import *
from random import randint


speed(0)
penup()
goto(-140,140)

for steps in range(15):
	write(steps, "	", align="center")
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)


ada = Turtle()
ada.color("red")
ada.shape("turtle")

bob = Turtle()
bob.color("blue")
bob.shape("turtle")

jen = Turtle()
jen.color("cyan")
jen.shape("turtle")

jim = Turtle()
jim.color("green")
jim.shape("turtle")

ben = Turtle()
ben.color("purple")
ben.shape("turtle")


ada.penup()
ada.goto(-160,110)
ada.right(360)
ada.pendown()

bob.penup()
bob.goto(-160,80)
bob.left(360)
bob.pendown()

jen.penup()
jen.goto(-160,50)
jen.right(360)
jen.pendown()

jim.penup()
jim.goto(-160,30)
jim.left(360)
jim.pendown()

ben.penup()
ben.goto(-160,0)
ben.right(360)
ben.pendown()


for turn in range(75):
	ada.forward(randint(1,15))
	bob.forward(randint(1,15))
	jen.forward(randint(1,15))
	jim.forward(randint(1,15))
	ben.forward(randint(1,15))
	



