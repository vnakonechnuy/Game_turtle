from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard:
    def __init__(self):
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.pendown()
        self.scoreboard.speed('fastest')
        self.scoreboard.penup()
        self.scoreboard.goto(-270, 250)

    def write_score(self, level, lives):
        self.scoreboard.clear()
        self.scoreboard.write(f'Level: {level}\nLives: {lives}', font=FONT)

    def game_over(self):
        self.scoreboard.goto(-100, 0)
        self.scoreboard.write('GAME IS OVER', font=('Arial', 25, 'normal'))