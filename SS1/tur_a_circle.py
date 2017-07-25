from turtle import *
from random import *
speed(0)
colormode(255)
for side_n in range(15,2,-1):
    color((randint(1, 255),randint(1, 255),randint(1, 255)),(randint(1, 255),randint(1, 255),randint(1, 255)))
    begin_fill()
    for i in range(side_n):
        forward(100)
        left(360/side_n)
    end_fill()
