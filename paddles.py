from turtle import Turtle


# Get the Paddles class to inherit from the Turtle Class.
class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # def create_paddles(self, x, y):
    #     # Create a paddle
    #     paddle = Turtle()
    #     self.shape("square")
    #     self.color("white")
    #     self.shapesize(stretch_wid=5, stretch_len=1)
    #     self.penup()
    #     self.goto(x, y)

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
