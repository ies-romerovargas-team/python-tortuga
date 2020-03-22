import turtle

def espiral(tortuga, size, decrement):
    for j in range(size//(decrement*4)):
        for i in range(4):
            tortuga.speed(0)
            tortuga.forward(size)
            tortuga.left(90)
            size = size - decrement

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Espiral")

t1 = turtle.Turtle()
espiral(t1, 200, 3)

wn.exitonclick()