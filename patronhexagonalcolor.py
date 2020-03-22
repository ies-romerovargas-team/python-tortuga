import turtle

def patron(tortuga):
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    for j in range(200):
        tortuga.forward(j)
        tortuga.left(59)
        tortuga.color(colors[j%6])

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Patrón creciente")

t1 = turtle.Pen()
t1.pensize(1)
t1.speed(0)
t1.color('blue')
patron(t1)

wn.exitonclick()

