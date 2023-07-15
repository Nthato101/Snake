from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.placement = self.new_food()

    def new_food(self):
        x = random.randrange(-470,470)
        y = random.randrange(-365,365)
        coordinate = self.goto(x=x,y=y)
        return coordinate


