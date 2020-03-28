import turtle

# leer datos
handle = open("tortuga/coronavirus/datos.txt")
fecha = list()
casos = list()
hospital = list()
uci = list()
fallecidos = list()

cont = 0
for line in handle:
    linea = line.split("\t")
    if cont > 0 :
        fecha.append(linea[0])
        casos.append(int(linea[1]))
        hospital.append(int(linea[2]))
        uci.append(int(linea[3]))
        finados = linea[4].rstrip("\n")
        fallecidos.append(int(finados))
    cont += 1

max_casos = max(casos)

wm = turtle.Screen()
wm.setup(800, 400)
wm.setworldcoordinates(0, 0, (cont - 1), (max_casos + 1000))

ejeX = turtle.Turtle()


grafica = turtle.Turtle()
for x in range(cont-1):
    grafica.goto(x, casos[x])
    grafica.dot()
    grafica.write(casos[x])

wm.exitonclick()