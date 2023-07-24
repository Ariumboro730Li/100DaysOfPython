import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

from turtle import Turtle, Screen


def move(turtle):
    turtle.left(50)
    turtle.forward(100)


sia = Turtle()
sia.shape("turtle")
sia.color("red")
sia.forward(100)
move(sia)
move(sia)
move(sia)
move(sia)
move(sia)
move(sia)
move(sia)
move(sia)
move(sia)

print(sia)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
