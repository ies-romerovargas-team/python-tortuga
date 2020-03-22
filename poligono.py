import turtle

def poligono(tortuga, side, side_lenght):
    for i in range(side):
        tortuga.forward(side_lenght)
        tortuga.right(360/side)

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("orange")
wn.title("Polígono de n lados")

t1 = turtle.Turtle()
poligono(t1, 8, 100)

wn.exitonclick()