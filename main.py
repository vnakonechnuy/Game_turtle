import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
me = Player()
car_manager = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(me.move_up, 'w')
screen.onkey(me.move_down, 's')


game_is_on = True
while me.lives > 0:
    scoreboard.write_score(car_manager.level, me.lives)
    car_manager.new_car()
    car_manager.move()
    time.sleep(0.1)
    screen.update()

    for car in car_manager.all_car:
        if car.distance(me) < 20:
            print(f'BOom')
            print(f'Lives = {me.lives}')
            me.lives -= 1
            me.start()

    if me.ycor() >= 280:
        me.start()
        me.lives += 1
        car_manager.level_up()

scoreboard.game_over()
screen.exitonclick()