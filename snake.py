from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.position = (0,0)
        self.segments = []
        self.initialize_snake()
        self.head = self.segments[0]

    def initialize_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend_snake(self):
        self.add_segment(self.segments[-1].pos())

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
            seg.goto(1000, 1000)
        self.segments.clear()
        self.initialize_snake()
        self.head = self.segments[0]
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[seg_num - 1].pos()
            self.segments[seg_num].setpos(new_position)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
