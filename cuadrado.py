import turtle

def cuadrado(tortuga, side):
    for i in range(4):
        tortuga.forward(side)
        tortuga.right(90)

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("orange")
wn.title("Cuadrado")

t1 = turtle.Turtle()
cuadrado(t1,100)

wn.exitonclick()