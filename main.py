from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)


'''screen.tracer will trace the steps and 
do nothing when screen.update mentioned 
it will update the traced path'''


snake = Snake()
food = Food()
sc = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_on = True
while game_on:
    sleep(0.1)
    screen.update()

    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        sc.increase_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280:
        sc.reset()
        snake.reset()
    if snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        sc.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        # if segment == snake.segments[0]:
        #     pass
        # snake.segments = snake.segments[1:]

        if snake.segments[0].distance(segment) < 10:
            sc.reset()
            snake.reset()


screen.exitonclick()
