from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as high:
            self.high_score = int(high.read())

        self.color('white')
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear_c()
        self.write(f'Score: {self.score} High Score: {self.high_score}',
                   align='center',
                   font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear_c()
        self.write(f'Score: {self.score} High Score: {self.high_score}',
                   align='center',
                   font=('Arial', 24, 'normal'))

    def clear_c(self):
        self.clear()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as high:
                high.write(str(self.high_score))
        self.score = 0
        self.update_score()