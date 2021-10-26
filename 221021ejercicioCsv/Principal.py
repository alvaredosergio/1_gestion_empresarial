from cliente import *

file = open("datos.csv")
line = file.readline()

clientes = []

while line != "":
    data = line.split(";")
    cl = Cliente(data[0],data[1],[float(data[2]),float(data[3]),float(data[4]),float(data[5])],data[6])
    clientes.append(cl)
    line = file.readline()
file.close()

print("Clientes con salgo negativo: ")
for cl in clientes:
    for mes in cl.meses:
        if mes <= -200:
            print(cl.nombre)
            break





