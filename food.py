from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("blue")
        self.refresh()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))
