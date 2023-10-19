from turtle import Turtle

SCOREBOARD = 0

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.color("white")
    self.score = SCOREBOARD
    self.goto(0, 270)
    self.refresh()

  def refresh(self):
    self.clear()
    self.write(f"Score= {self.score}", align="center", font=("Arial", 16, "normal"))

  def add_score(self):
    self.score += 1
    self.refresh()