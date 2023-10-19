from part6.snake import Snake
from part6.food import Food
from part6.socreboard import Scoreboard
import time
from turtle import Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  #collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.add_score()
    #extend snake after eat 2 times
    if scoreboard.score % 2 == 0:
      snake.extend()

  #detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    print("Wall Collision!")
    game_is_on = False
    scoreboard.game_over()


  #detect collision with tail
  #if head collides with any segment in the tail - trigger game_over
  for segment in snake.snake_body:
    if segment == snake.head:
      pass
    elif snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()
    


screen.exitonclick()
