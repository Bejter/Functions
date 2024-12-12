import turtle

def draw_square(length):
# Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")
# Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

# Draw a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

# Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()
def draw_triangle(r):
# Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")
# Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)
#Draw a triangle
    for i in range(3):
        pen.forward(r)
        pen.left(120)
# Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()

def draw_rectangle(a, b):
# Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")
# Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)
#Draw rectangle
    for i in range(2):
        pen.forward(a)
        pen.right(90)
        pen.forward(b)
        pen.right(90)
# Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()
