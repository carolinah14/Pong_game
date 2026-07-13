from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def collision_with_wall(self):
        return self.ycor() > 280 or self.ycor() < -280

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def collision_with_paddles(self, rpaddle, lpaddle):
        return (
                (self.distance(rpaddle) < 50 and self.xcor() > 320)
                or
                (self.distance(lpaddle) < 50 and self.xcor() < -320)
        )

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.move_speed *= 0.9
        self.bounce_x()
        self.random_y_serve()

    def random_y_serve(self):
        velocity = [10, -10]
        self.y_move = random.choice(velocity)

