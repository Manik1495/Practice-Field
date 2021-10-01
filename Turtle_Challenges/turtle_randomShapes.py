from turtle import Turtle, Screen

t = Turtle()

# def square():
#     for _ in range(4):
#         t.forward(100)
#         t.right(90)
#
# def pentagon():
#     for _ in range(5):
#         t.forward(100)
#         t.right(72)
#
# def hexagon():
#     for _ in range(6):
#         t.forward(100)
#         t.right(60)
#
# def heptagon():
#     for _ in range(7):
#         t.forward(100)
#         t.right(360/7)
#
# def octagon():
#     for _ in range(7):
#         t.forward(100)
#         t.right(360/7)

def shape(sides, color):
    for _ in range(sides):
        t.pencolor(color)
        t.forward(100)
        t.right(360 / sides)

shape(4,"brown")
shape(5,"green")
shape(6,"yellow")
shape(7,"blue")
shape(8,"orange")
shape(9,"red")
shape(10,"maroon")


# pentagon()
# hexagon()
# heptagon()
screen = Screen()
screen.exitonclick()