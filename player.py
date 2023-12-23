from turtle import bgcolor, circle, done, forward, hideturtle, pencolor, right, speed
speed(0)
bgcolor('black')
pencolor('steelblue')
for i in range(100):
    right(1)
    circle(200,1)
    forward(i)
    right(90)
    forward(i)
hideturtle()
done()