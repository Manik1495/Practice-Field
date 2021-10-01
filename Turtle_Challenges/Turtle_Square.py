from turtle import Turtle, Screen

tommy_turtle = Turtle()

tommy_turtle.shape("turtle")

for i in range(1,5):
    tommy_turtle.forward(100)
    tommy_turtle.right(90)



tommy_screen = Screen()
tommy_screen.exitonclick()

