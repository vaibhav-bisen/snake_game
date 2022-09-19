from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("dark green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-277, 277)
        random_y = random.randint(-277, 275)
        self.goto(random_x, random_y)
