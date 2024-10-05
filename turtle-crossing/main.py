import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move_car()
    
    for x in car.all_cars:
        if x.distance(player) < 20:
            game_is_on = False 
            scoreboard.game_over()
    
    if player.is_at_end():
        player.refresh()
        car.level_up()
        scoreboard.increase_level()
            
screen.exitonclick()