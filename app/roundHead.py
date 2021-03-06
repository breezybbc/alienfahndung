from alienfahndung.app.polyHead import *


class Round:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.ht()
        self.turtle.speed(10)
        self.turtle.up()
        self.turtle.goto(0, 0)
        self.turtle.down()

    section = 100

    def draw_round_head(self, radius, colour):
        self.turtle.up()
        self.turtle.goto(0, self.section)
        self.turtle.down()
        self.turtle.color("black", colors[int(colour)])
        self.turtle.begin_fill()
        self.turtle.circle(radius)
        self.turtle.end_fill()

    def set_section(self, value):
        self.section = value
