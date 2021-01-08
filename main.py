import turtle
import paddle
import scoreboard
import ball

screen = turtle.Screen()
screen.setup(width=2000, height=1000)
screen.bgcolor('black')
screen.title("Kemal's Pong Project")

paddles = paddle.Paddle()
balls = ball.Ball()
scoreboards = scoreboard.Scoreboard()

screen.listen()
screen.onkey(paddles.left_up, 'w')
screen.onkey(paddles.left_down, 's')
screen.onkey(paddles.right_up, 'Up')
screen.onkey(paddles.right_down, 'Down')
game_is_on = True

while game_is_on:
	balls.start()

	if balls.ycor() > 430 or balls.ycor() < -430:
		balls.change_trajectory_y()

	if balls.distance(paddles.right_paddles[0]) < 50 and balls.xcor() > 470 or balls.distance(paddles.left_paddles[0]) < 50 and balls.xcor() < 470:
		balls.change_trajectory_x()

	if balls.xcor() == paddles.left_paddles[0].xcor() - 40:
		balls.reset()
		scoreboards.paddles_score_up('right')
		balls.start()

	elif balls.xcor() == paddles.right_paddles[0].xcor() + 40:
		balls.reset()
		scoreboards.paddles_score_up('left')
		balls.start()

	if scoreboards.left_paddle_score == 10 or scoreboards.right_paddle_score == 10:
		game_is_on = False
		scoreboards.game_over()


screen.exitonclick()
