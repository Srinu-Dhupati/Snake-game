from turtle import  Screen
import time
from snake import Snake
from Food import Food
from Score import Score
# creaking border

snake = Snake()
food = Food()
score = Score()
# tim = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)


# creating snake shape
# all_positions = [(0, 0), (-20, 0), (-40, 0)]
# all_snakes = []

game_over = True



user_bet = screen.textinput(title="chose your level", prompt="easy or medium or hard").lower()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Left")
screen.onkey(snake.move_left, "Right")

screen.setup(width=500, height=500)
# snake movement
while game_over:
    screen.update()
    if user_bet == "easy":
        time.sleep(0.4)
    elif user_bet == "medium":
        time.sleep(0.2)
    elif user_bet == "hard":
        time.sleep(0.1)
    snake.move()

    # detecting food collision and score board
    if snake.head.distance(food)<15:
        score.increase_score()
        food.refresh()
        snake.extend()

    # detecting collision with walls
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290
            or snake.head.ycor() < -290):
        game_over = False
        score.game_over()

    # detecting collision with its own tail
    for segment in snake.all_snakes[1:]:
        if snake.head.distance(segment) < 15:
            game_over = False
            score.game_over()





screen.exitonclick()