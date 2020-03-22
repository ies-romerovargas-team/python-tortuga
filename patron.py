import turtle

def patron(tortuga):    
    for j in range(200):
        tortuga.forward(j)
        tortuga.right(88)        

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Patrón creciente")

t1 = turtle.Turtle()
t1.pensize(1)
t1.speed(0)
patron(t1)

wn.exitonclick()