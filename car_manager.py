from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 7
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_car = []
        self.level = 1

    def new_car(self):
        random_chance = random.randint(self.level, 6)
        if random_chance == 6:
            car = Turtle('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.speed('fastest')
            car.color(random.choice(COLORS))
            car.goto(x=280, y=random.randint(-250, 250))
            car.setheading(180)
            self.all_car.append(car)

    def move(self):
        for car in self.all_car:
            car.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.level += 1
        self.new_car()

