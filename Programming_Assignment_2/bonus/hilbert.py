from turtle import Turtle, Screen
from PIL import Image
import os

def Hilbertcurve(length, facing, size, turtle):
    if size < 1:
        return
    turtle.left(facing * 90)
    Hilbertcurve(length, -facing, size-1, turtle)
    turtle.forward(length)

    turtle.right(facing * 90)
    Hilbertcurve(length, facing, size-1, turtle)
    turtle.forward(length)

    Hilbertcurve(length, facing, size-1, turtle)
    turtle.right(facing * 90)
    turtle.forward(length)

    Hilbertcurve(length, -facing, size-1, turtle)
    turtle.left(facing * 90)

def save_image(turtle, filename):
    canvas = turtle.getscreen().getcanvas()
    ps_filename = filename + '.ps'
    canvas.postscript(file=ps_filename, colormode='color')
    with Image.open(ps_filename) as img:
        img.save(filename + '.png', 'PNG')
    os.remove(ps_filename)

def main():
    screen = Screen()
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color("red")
    turtle.speed(0)
    for size in range(1, 5):
        Hilbertcurve(10, 1, size, turtle)
        save_image(turtle, f"h_{size}")
        turtle.clear()

main()
