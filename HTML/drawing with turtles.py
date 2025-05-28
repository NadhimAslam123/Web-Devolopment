import turtle

t = turtle.Turtle()

for _ in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(150, 0)
t.pendown()

for _ in range(2):
    t.forward(120)
    t.left(90)
    t.forward(60)
    t.left(90)

turtle.done()