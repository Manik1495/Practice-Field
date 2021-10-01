from turtle import Turtle, right

#DECLARING CONSTANTS HERE
STARTING_POSITION = [(0, 0),(-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        # add the segment to the last position of the segment list
        # position() gives the position of the segment[-1]
        self.add_segment(self.segments[-1].position())


    def snake_move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            # new_x = segments[2 - 1].xcor()
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    
    def up(self):
        # turtle.left(67)
        # >>> turtle.heading()
        # 67.0
        # setheading()-->Set the orientation of the turtle to to_angle. 
        # Here are some common directions in degrees:
        if self.head.heading() != DOWN:
            # this if statement -->
            #  you cant reverse your direction directly.
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

