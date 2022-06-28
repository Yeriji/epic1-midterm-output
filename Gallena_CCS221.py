import turtle as t

t.speed (0)

t. tracer (10)

t.bgcolor('black')

color=('steelblue','coral','magenta','palegreen')
for i in range(800):
    t.pencolor(color[i%4])
    t.pensize(0.8)
    t.backward(i)
    t.rt(120)
    t.circle(60)
    t.right(90)

t.exitonclick()