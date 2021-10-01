from turtle import Turtle

FONT = (('Courier', 15, 'bold'))
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.new_score = 0
        
        self.hideturtle()
        self.goto(0,280)
        self.color("white")
        self.increase_score()

    def increase_score(self):
        # to start displaying score with "0"
        self.write(f"Score: {self.new_score}", font=FONT, align = ALIGNMENT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"SNAKE GAME OVER", font=FONT, align = ALIGNMENT)


    def update_scoreboard(self):
        
        self.new_score += 1
        self.clear()
        # continue with increasing score
        self.increase_score()
        
        
