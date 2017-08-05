from turtle import *
speed(0)

"""define a fuction draw a star with length and (x,y) 2 dimentions Cartesian Coordinates is parameter"""

def draw_star(x, y , length):
	penup()
	goto(x,y)
	pendown()
	for i in range(5):
		left(-144)
		forward(length)
		
# draw Nam's star
draw_star(1,1,50)
# Draw Hiệp's star
# length quá bé
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

# a = input()