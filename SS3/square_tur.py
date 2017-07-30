from turtle import *
speed(0)
shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(6):
	# for j in range(1,3)
	color(colors[i])
	begin_fill()
	for j in range(4):
		if (j%2)==1:
			forward(100)
		else:
			forward(50)
		left(360/4)
	end_fill()
	forward(50)
