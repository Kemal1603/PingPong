import turtle


class Paddle:

	def __init__(self):
		self.left_paddles = []
		self.right_paddles = []
		self.create_paddles()
		self.colorize_paddles()

	def create_paddles(self):
		left_paddle = turtle.Turtle('square')
		left_paddle.shapesize(stretch_wid=5, stretch_len=1)
		left_paddle.penup()
		left_paddle.goto(-950, 0)
		self.left_paddles.append(left_paddle)

		right_paddle = turtle.Turtle('square')
		right_paddle.shapesize(stretch_wid=5, stretch_len=1)
		right_paddle.penup()
		right_paddle.goto(940, 0)
		self.right_paddles.append(right_paddle)

	def colorize_paddles(self):
		for paddle in self.left_paddles:
			paddle.color('white')
		for paddle in self.right_paddles:
			paddle.color('white')

	def left_up(self):
		new_y = self.left_paddles[0].ycor() + 40
		self.left_paddles[0].goto(self.left_paddles[0].xcor(), new_y)

	def left_down(self):
		new_y = self.left_paddles[0].ycor() - 40
		self.left_paddles[0].goto(self.left_paddles[0].xcor(), new_y)

	def right_up(self):
		new_y = self.right_paddles[0].ycor() + 40
		self.right_paddles[0].goto(self.right_paddles[0].xcor(), new_y)

	def right_down(self):
		new_y = self.right_paddles[0].ycor() - 40
		self.right_paddles[0].goto(self.right_paddles[0].xcor(), new_y)
