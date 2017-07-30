from turtle import *
speed(0)
shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
shape_n = 3
for a in range(shape_n,shape_n+len(colors)):
	color(colors[a-3])
	for i in range(shape_n):
		forward(100)
		left(360/shape_n)
	shape_n+=1
for i in range(6):
	# for j in range(1,3)
	color(colors[i])
	begin_fill()
	for j in range(4):
		if j%2==1:
			forward(50)
		else:
			forward(100)
		left(360/4)
	end_fill()
	forward(50)


