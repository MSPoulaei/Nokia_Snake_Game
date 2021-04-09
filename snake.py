from turtle import Turtle


class Snake:
    def __init__(self):
        self.snakes = []
        x, y = 0, 0
        for i in range(3):
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x, y)
            self.snakes.append(new_snake)
            x -= 20

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i].goto(self.snakes[i - 1].xcor(), self.snakes[i - 1].ycor())
        self.snakes[0].forward(20)

    def right(self):
        intended_heading = 0
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(intended_heading)

    def up(self):
        intended_heading = 90
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(intended_heading)

    def left(self):
        intended_heading = 180
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(intended_heading)

    def down(self):
        intended_heading = 270
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(intended_heading)
    def increase_length(self):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(self.snakes[-1].xcor(),self.snakes[-1].ycor())
        self.snakes.append(new_snake)