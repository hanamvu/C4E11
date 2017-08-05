from turtle import *
speed(0)
"""define a fuction draw a square with length and color is parameter"""
def draw_square(length, _color):
	color(_color)
	for i in range(4):
		forward(length)
		left(90)

draw_square(100,"green")

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()