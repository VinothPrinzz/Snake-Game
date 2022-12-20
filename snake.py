from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):

    def __init__(self):
        self.segments = []
        super().__init__()
        self.create_snake()

    def create_snake(self):

        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle()
        tim.penup()
        tim.shape('square')
        tim.color('white')
        tim.speed('fastest')
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.speed(10000)
        self.add_segment(self.segments[-1].position())

    def move(self):
        for tur_no in range(len(self.segments) - 1, 0, -1):
            x = self.segments[tur_no - 1].xcor()
            y = self.segments[tur_no - 1].ycor()
            self.segments[tur_no].goto(x=x, y=y)
        '''32 this is position right 
            now 1 is overlapped by 2, so we move 
            1 forward after loop and update, final 321'''

        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

