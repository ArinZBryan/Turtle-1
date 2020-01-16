import turtle;import random
screen=turtle.Screen()
TurtleScript1= turtle.Turtle()
TurtleScript1. shape("turtle")
TurtleScript1.speed(999999999999999999999)
for j in range(180):
	TurtleScript1.rt(2)
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	for i in range(12):
		TurtleScript1.fd(30)
		TurtleScript1.rt(30)
		TurtleScript1.pencolor(r,g,b)
