import turtle
import os

win = turtle.Screen()
win.title('Pong by Erika')
win.bgcolor("black")
win.setup(width=800, height=600)
# stops window from updating - runs faster or something??
win.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('pink')
paddle_a.shapesize(stretch_wid=5, stretch_len= 1)
paddle_a.penup()
# paddle starting point
paddle_a.goto((-350, 0))


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('pink')
paddle_b.shapesize(stretch_wid=5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto((350, 0))

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('red')
ball.penup()
# ball starting point
ball.goto((0, 0))
# direction ball moves in (diagonal)
ball.dx = 0
ball.dy = 0

# Score
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Press space to start', align='center', font=('Courier', 20, 'normal'))


def start_game():
    if ball.dx == 0 and ball.dy == 0:
        pen.clear()
        pen.write('Player A: 0   Player B: 0', align='center', font=('Courier', 20, 'normal'))
        ball.dx = 3
        ball.dy = -3

def end_game():
    ball.goto((0, 0))
    ball.dx = 0
    ball.dy = 0
    pen.clear()
    pen.write('Press space to start', align='center', font=('Courier', 20, 'normal'))


# Moving the paddles

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding

# listen - widow listens to keyboard inputs
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')
win.onkeypress(start_game, 'space')
win.onkeypress(end_game, 'Escape')


# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boarder checking

    # top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay wall_bounce.wav&")
    # bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay wall_bounce.wav&")
    # right
    if ball.xcor() > 410:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))
    # left
    if ball.xcor() < -410:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))

    # Paddle bounce

    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -45):
        # ( front surface back surface? )       AND  ( ball cord              paddle length 40)
        ball.setx(330)
        ball.dx *= -1
        os.system("afplay paddle_bounce.wav&")

    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < paddle_a.ycor() + 45 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-330)
        ball.dx *= -1
        os.system("afplay paddle_bounce.wav&")

    if (ball.xcor() == 0 and ball.ycor() == 0) and (ball.dx == 0 and ball.dy == 0):
        score_a = 0
        score_b = 0

    if score_a == 3:
        ball.dx = 0
        ball.dy = 0
        pen.clear()
        pen.write('Player A WINS!', align='center', font=('Courier', 20, 'normal'))

    if score_b == 3:
        ball.dx = 0
        ball.dy = 0
        pen.clear()
        pen.write('Player B WINS!', align='center', font=('Courier', 20, 'normal'))
