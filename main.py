import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

window = Screen()
window.setup(width=1000, height=750)
window.bgcolor("black")
window.title("SnakeGame")
window.tracer(0)

# def extend_body(list):

snake = Snake()
snake_body = snake.body
food = Food()

scoreboard = Score()

game_on = True

while game_on:

    window.update()
    time.sleep(0.1)
    snake.move()
    window.listen()
    window.onkey(key="Up", fun=snake.move_up)
    window.onkey(key="Down",fun=snake.move_down)
    window.onkey(key="Left",fun=snake.move_left)
    window.onkey(key="Right",fun=snake.move_right)

    if snake.head.distance(food) < 15:
        food.new_food()
        scoreboard.score_count()
        snake.extend_body()

    if snake.head.xcor() > 495 or snake.head.xcor() < -495 or snake.head.ycor() > 370 or snake.head.ycor() < -370:
        scoreboard.game_over()
        game_on = False

    for index in range(1, len(snake_body)-1):
        if snake.head.distance(snake_body[index]) < 10:
            scoreboard.game_over()
            game_on = False

window.exitonclick()
