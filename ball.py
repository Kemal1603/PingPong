import turtle


class Ball(turtle.Turtle):

	def __init__(self):
		super().__init__()
		self.shape('circle')
		self.penup()
		self.shapesize(stretch_wid=1.5, stretch_len=1.5)
		self.color('red')
		self.trajectory_x = 10
		self.trajectory_y = 10

	def start(self):
		new_x = self.xcor() + self.trajectory_x
		new_y = self.ycor() + self.trajectory_y
		self.speed('slow')
		self.goto(new_x, new_y)

	def change_trajectory_y(self):
		self.trajectory_y *= -1

	def change_trajectory_x(self):
		self.trajectory_x *= -1

	def reset(self):
		self.hideturtle()
		self.goto(0, 0)
		self.showturtle()
		self.change_trajectory_x()

