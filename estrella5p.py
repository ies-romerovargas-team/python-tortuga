import turtle

def estrella(tortuga, side):
    for i in range(5):
        tortuga.forward(side)
        tortuga.right(144)

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("orange")
wn.title("Estrella de 5 puntas")

t1 = turtle.Turtle()
estrella(t1, 200)

wn.exitonclick()