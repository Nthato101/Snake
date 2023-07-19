from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 338)
        self.color("White")
        self.score_update()

    def score_count(self):
        self.clear()
        self.score += 1
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(arg=f" Score: {self.score}  High Score: {self.high_score}", move=False, align="Center",
                   font=("Arial", 12, "bold"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", move=False, align="Center", font=("Arial", 12, "bold"))

    def high_score_update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.score_update()
