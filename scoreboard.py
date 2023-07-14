from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 338)
        self.color("White")
        self.score_update()


    def score_count(self):
        self.score += 1
        self.clear()
        self.score_update()

    def score_update(self):
        self.write(arg=f" Score: {self.score}", move=False, align="Center", font=("Arial", 12, "bold"))

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(arg=f"Game Over", move=False, align="Center", font=("Arial", 12, "bold"))

