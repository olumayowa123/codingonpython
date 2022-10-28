import turtle

screen = turtle.Screen()
screen.bgcolor("cyan")

sam = turtle.Turtle()
sam.shape("turtle")
sam.color('red')
sam.begin_fill()
for i in range(4):
    sam.fd(50)
    sam.left(90)
sam.end_fill()
