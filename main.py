from turtle import Screen
from time import sleep
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")

game_is_over = False
while not game_is_over:
    sleep(.1)
    snake.move()
    screen.update()
    if snake.snakes[0].distance(food) < 20:
        scoreboard.increase_score()
        scoreboard.update()
        food.refresh()
        snake.increase_length()
    elif snake.snakes[0].xcor()>280 or snake.snakes[0].xcor()<-280 or\
            snake.snakes[0].ycor()>280 or snake.snakes[0].ycor()<-280:
        game_is_over = True
        scoreboard.game_over()
    for i in range(1,len(snake.snakes)):
        if snake.snakes[0].distance(snake.snakes[i])<15:
            game_is_over = True
            scoreboard.game_over()
            break
screen.exitonclick()
