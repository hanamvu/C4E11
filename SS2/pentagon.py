from turtle import *
shape("turtle")
speed(0)
shape_n = 3
for a in range(shape_n,7):
	if (shape_n%2 ==0):
		color("red")
	else:
		color("blue")
	for i in range(shape_n):
		forward(100)
		left(360/shape_n)
	shape_n+=1
