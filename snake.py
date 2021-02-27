from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.snake.append(tim)

    def extend_segment(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for s in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[s - 1].xcor()
            new_y = self.snake[s - 1].ycor()
            self.snake[s].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
