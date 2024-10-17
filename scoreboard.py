from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", True, align=ALIGNMENT, font=('Courier', 35, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                self.high_score = file.write(str(self.high_score))
        self.score = 0
        self.display_score()