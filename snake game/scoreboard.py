from turtle import Turtle
with open("hight_score.txt", mode="r") as score_sheet:
    old_high_score = int(score_sheet.read())
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = old_high_score
        self.hideturtle()
        self.color("white")
        self.sc = 0
        self.penup()
        self.goto(0, 280)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score = {self.sc} High Score: {self.high_score}", False,"center")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, "center")

    def reset(self):
        if self.high_score < self.sc:
            self.high_score = self.sc
            with open("hight_score.txt", mode="w") as score_sheet_new:
                score_sheet_new.write(f"{self.high_score}")

        self.sc = 0
        self.update_score_board()
