import os
from producto import Producto
from componente import Componente
from csv import *


def produccionMensual():
    file = open("csv/productos.csv",'r')
    line = file.readline()
    componentes = []
    while line != "":
        lineaBuena = line.split("\n")[0]
        datos = lineaBuena.split(";")
        co = Componente(datos[1])
        componentes.append(co)
        line = file.readline()
        file.close()
        for cons in componentes:
            print(cons)

produccionMensual()

