import turtle

# leer datos
handle = open("datos.txt")
fecha = list()
casos = list()
hospital = list()
uci = list()
fallecidos = list()
recuperados = list()

cont = 0
for line in handle:
    linea = line.split("\t")
    if cont > 0 :
        fecha.append(linea[0])
        casos.append(int(linea[1]))
        hospital.append(int(linea[2]))
        uci.append(int(linea[3]))        
        fallecidos.append(int(linea[4]))
        aux = linea[5].rstrip("\n")
        recuperados.append(int(aux))
    cont += 1

max_casos = max(casos)

wm = turtle.Screen()
wm.title("coronavirus")
wm.setup(800, 400)
wm.setworldcoordinates(0, 0, (cont + 2), (max_casos + (max_casos/cont)))

marco = turtle.Turtle()
marco.penup()
marco.goto(1, 500)
marco.pendown()
marco.fillcolor("pink")
marco.begin_fill()
marco.goto(cont - 1, 500)
marco.goto(cont - 1, max_casos + 250)
marco.goto(1, max_casos + 250)
marco.goto(1, 500)
marco.end_fill()

ejeX = turtle.Turtle()
ejeX.hideturtle()
ejeX.penup()
ejeX.goto(1, 500)
ejeX.pendown()

ejeY = turtle.Turtle()
ejeY.hideturtle()
ejeY.color("red")
ejeY.penup()
ejeY.goto(1, 500)
ejeY.pendown()

ejeY2 = turtle.Turtle()
ejeY2.hideturtle()
ejeY2.color("blue")
ejeY2.penup()
ejeY2.goto(cont - 1, 500)
ejeY2.pendown()

for x in range(10):
    #ejeY.goto(1, casos[x] + 500)
    ejeY.goto(1, 10000 * x)
    ejeY.dot()
    ejeY.write(10000 * x, False, "right")

    ejeY2.goto(cont - 1, (x * 1000 * (max(casos)/max(fallecidos))))
    ejeY2.dot()
    ejeY2.write(x * 1000, False, "left")

grafica1 = turtle.Turtle()
grafica1.color("red")
grafica1.width(2)
grafica1.hideturtle()
grafica1.penup()
grafica1.goto(1, 500)
grafica1.pendown()

grafica2 = turtle.Turtle()
grafica2.color("blue")
grafica2.width(2)
grafica2.hideturtle()
grafica2.penup()
grafica2.goto(1, 500)
grafica2.pendown()

for x in range(cont - 1):
    
    grafica1.goto(x + 1, casos[x] + 500)
    grafica1.dot()
    #grafica1.write(casos[x], False, "right")
    
    grafica2.goto(x + 1, (fallecidos[x] * max(casos)/max(fallecidos) + 500))
    grafica2.dot()
    #grafica2.write(fallecidos[x], False, "left")

    ejeX.goto(x + 1, 0)
    ejeX.dot()
    ejeX.write(fecha[x][0:2], False, "center")
    
wm.exitonclick()