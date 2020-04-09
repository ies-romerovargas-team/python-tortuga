import turtle

# leer datos
handle = open("datos_abs.txt")
fecha = list()
casos = list()
hospital = list()
uci = list()
fallecidos = list()
recuperados = list()

cont = 0
for line in handle:
    linea = line.split("\t")
    if cont > 0 : # la primera línea no, gracias
        fecha.append(linea[0])
        casos.append(int(linea[1]))
        hospital.append(int(linea[2]))
        uci.append(int(linea[3]))        
        fallecidos.append(int(linea[4]))
        aux = linea[5].rstrip("\n")
        recuperados.append(int(aux))
    cont += 1
handle.close()

max_casos = max(casos)

ancho = 800
alto = 400
margen = 20

wm = turtle.Screen()
wm.title("coronavirus")
wm.setup(ancho, 400)  
wm.setworldcoordinates(0, 0, ancho, alto)

marco = turtle.Turtle()
marco.penup()
marco.hideturtle()
marco.speed(0)
marco.goto(margen, margen)
marco.pendown()
marco.fillcolor("GhostWhite")
marco.begin_fill()
marco.goto(ancho - margen * 2, margen)
marco.goto(ancho - margen * 2, alto - margen * 2)
marco.goto(margen, alto - margen * 2)
marco.goto(margen, margen)
marco.end_fill()

ejeX = turtle.Turtle()
ejeX.hideturtle()
ejeX.penup()
ejeX.goto(margen, margen)
ejeX.pendown()

ejeX2 = turtle.Turtle()
ejeX2.hideturtle()
ejeX2.penup()
ejeX2.goto(margen, 0)

ejeY = turtle.Turtle()
ejeY.hideturtle()
ejeY.color("red")
ejeY.penup()
ejeY.goto(margen, margen)
ejeY.pendown()

ejeY2 = turtle.Turtle()
ejeY2.hideturtle()
ejeY2.color("blue")
ejeY2.penup()
ejeY2.goto(ancho - margen * 2, margen)
ejeY2.pendown()

coeficienteX = (ancho - margen * 2) / cont
coeficienteY = (alto - margen * 3) / max(casos)
coeficienteY2 = (alto - margen * 3) / max(fallecidos)

for x in range(0, max(casos), 1000):    
    ejeY.goto(margen, margen + (x * coeficienteY)) 
    ejeY.dot()
    ejeY.write(x, False, "right")

for x in range(0, max(fallecidos), 100):    
    ejeY2.goto(ancho - margen * 2, margen + (x * coeficienteY2))
    ejeY2.dot()
    ejeY2.write(x, False, "left")

grafica1 = turtle.Turtle()
grafica1.color("red")
grafica1.width(3)
grafica1.hideturtle()
grafica1.penup()
grafica1.goto(margen, margen)
grafica1.pendown()

grafica2 = turtle.Turtle()
grafica2.color("blue")
grafica2.width(3)
grafica2.hideturtle()
grafica2.penup()
grafica2.goto(margen, margen)
grafica2.pendown()

mes = "00"
for x in range(cont - 1):
    
    grafica1.goto(x * coeficienteX + margen, margen + (casos[x] * coeficienteY))
    grafica1.dot()
    if(casos[x] > 100):
        grafica1.write(casos[x], False, "right")
    
    grafica2.goto(x * coeficienteX + margen, margen + (fallecidos[x] * coeficienteY2))
    grafica2.dot()
    if(fallecidos[x]> 10):
        grafica2.write(fallecidos[x], False, "right")
        
    ejeX.goto(x * coeficienteX + margen, margen)
    ejeX.dot()
    if x%2!=0:
        ejeX2.goto(x * coeficienteX + margen, 0)
        ejeX2.write(fecha[x][0:2], False, "center")
        mes = fecha[x][3:2]

titulo1 = turtle.Turtle()
titulo1.hideturtle()
titulo1.penup()
titulo1.goto(margen * 2, alto - margen * 4)
titulo1.write("Datos Coronavirus", False, "left", "Arial 15")
titulo1.goto(margen * 2, alto - margen * 5)
titulo1.write("Actualizado a: " + fecha[x], False, "left")
titulo1.width(3)

titulo1.goto(margen * 2, alto - margen * 6)
titulo1.pendown()
titulo1.color("red")
titulo1.fd(100)
titulo1.penup()
titulo1.color("black")
titulo1.write(" Casos contabilizados", False, "left", "Arial 11")

titulo1.goto(margen * 2, alto - margen * 7)
titulo1.pendown()
titulo1.color("blue")
titulo1.fd(100)
titulo1.penup
titulo1.color("black")
titulo1.write(" Nº Fallecidos", False, "left", "Arial 11")

wm.exitonclick()