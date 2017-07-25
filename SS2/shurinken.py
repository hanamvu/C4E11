from turtle import *
color("red")
speed(0)
for i in range(4):
	for j in range(4):
		if(j/2 == 1):
			left(120)
		else:
			left(60)
		forward(100)
	left(-30)
