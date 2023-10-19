from turtle import Turtle

SCOREBOARD = 0
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

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
    self.write(f"Score= {self.score}", align=ALIGNMENT, font=FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)
  
  def add_score(self):
    self.score += 1
    self.refresh()