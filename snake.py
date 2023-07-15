from turtle import Turtle

direction = Turtle
move_length = 20


class Snake:

    def __init__(self):
        self.body = []
        self.create_body()
        self.head = self.body[0]
        self.move()

    def create_body(self):

        head1 = Turtle(shape="square")
        head1.color("white")
        head1.penup()
        head1.goto(x=0, y=0)

        head2 = Turtle(shape="square")
        head2.color("white")
        head2.penup()
        head2.goto(x=-20, y=0)

        head3 = Turtle(shape="square")
        head3.color("white")
        head3.penup()
        head3.goto(x=-40, y=0)

        self.body = [head1, head2, head3]

    def move(self):

        for body_index in range(len(self.body) - 1, 0, -1):
            new_x = self.body[body_index - 1].xcor()
            new_y = self.body[body_index - 1].ycor()
            self.body[body_index].goto(new_x, new_y)
        self.head.forward(move_length)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def extend_body(self):
        new_piece = self.body[-1].clone()
        new_piece.goto(self.body[-1].position())
        self.body.append(new_piece)






