import turtle


class Scoreboard(turtle.Turtle):

	def __init__(self):
		super().__init__()
		self.left_paddle_score = 0
		self.right_paddle_score = 0
		self.color('white')
		self.penup()
		self.hideturtle()
		self.goto(0, 400)
		self.showturtle()
		self.write(f"{self.left_paddle_score} | {self.right_paddle_score} ", move=False, align="center", font=("Arial", 40, "bold"))
		self.hideturtle()

	def paddles_score_up(self, side):
		if side == 'left':
			self.left_paddle_score += 1
			self.clear()
			self.write(f"{self.left_paddle_score} | {self.right_paddle_score} ", move=False, align="center", font=("Arial", 40, "bold"))
		elif side == 'right':
			self.right_paddle_score += 1
			self.clear()
			self.write(f"{self.left_paddle_score} | {self.right_paddle_score} ", move=False, align="center", font=("Arial", 40, "bold"))

	def game_over(self):
		self.clear()
		self.goto(0, 0)
		self.write(f"Игра окончена результат: {self.left_paddle_score} левый игрок | {self.right_paddle_score} правый игрок", move=False, align="center", font=("Arial", 20, "bold"))
