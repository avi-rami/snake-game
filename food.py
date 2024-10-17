from turtle import Turtle
import turtle
import random

class Food(Turtle):
    # food class will know how to render itself as a random circle on the screen
    # everytime the snake touches the food, it will move to a new random location
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5,stretch_len=.5)
        self.speed("fastest")
        # turtle.colormode(255)
        self.color("purple")
        self.refresh_food()

    def refresh_food(self):
        # self.color(self.random_color())
        random_x = random.randrange(-280, 280)
        random_y = random.randrange(-280, 280)
        self.setpos(random_x, random_y)

    # def random_color(self):
    #     color = (random.randint(0, 200), random.randint(0, 200), random.randint(0, 200))
    #     return color