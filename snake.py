from turtle import Turtle
tim = Turtle()

# a =[1, 2, 3, 4, 3, 4, 5]
# print(a[::-1]) # printing reverse of the list


all_positions = [(0, 0), (-20, 0), (-40, 0)]
up = 90
down = 270
right = 180
left = 0
tim.penup()
tim.color("white")
tim.goto(290, 290)
tim.hideturtle()
for i in range(5):
    tim.right(90)
    tim.pendown()
    tim.forward(580)

class Snake:
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for position in all_positions:
            self.add(position)

    def add(self, position):
        snake1 = Turtle(shape="square")
        snake1.penup()
        snake1.color("white")
        snake1.goto(position)
        self.all_snakes.append(snake1)

    def extend(self):
        self.add(self.all_snakes[-1].position())

    def move(self):
        for seg_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[seg_num - 1].xcor()  # here we swap the place of first square to 2nd square and 2nd
            # to 3rd
            # by using previous coardinates
            new_y = self.all_snakes[seg_num - 1].ycor()
            self.all_snakes[seg_num].goto(new_x, new_y)
        self.head.forward(20)
        if tim.xcor() > 500:
            game_over = False

    def move_up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def move_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def move_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def move_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
