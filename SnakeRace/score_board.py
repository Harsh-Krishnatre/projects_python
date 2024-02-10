from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setpos(0, 210)
        self.write(f"Score: {self.score}", True, "center", ("Courier", 20, "bold"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1
        self.setpos(0, 210)
        self.write(f"Score: {self.score}", True, "center", ("Courier", 20, "bold"))

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", True, "center", ("Courier", 50, "bold"))
