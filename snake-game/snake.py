from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.generate_snake()
        self.head = self.segments[0]
    def generate_snake(self):
        x = 0
        for count in range(0, 3):
            new_snake = Turtle("square")
            new_snake.penup()
            new_snake.color("white")
            new_snake.goto(x=x, y=0)
            self.segments.append(new_snake)
            x -= 20

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
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
