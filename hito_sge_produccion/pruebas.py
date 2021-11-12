from componente import *
from functions import visuCsvComponentes
from producto import *
import os

## VISUALIZAR PRODUCTOS
def visuCsvProductos():
    file = open("csv/productos.csv",'r')
    line = file.readline()
    productos = []
    while True:
        line = file.readline()
        if line == "":
            break
        lineaBuena = line.split("\n")[0]
        datos = lineaBuena.split(";")
        listaString = datos[2][2:len(datos[2])-2]
        listaFinal = []
        listaCompo = listaString.split("],[")
        for c in listaCompo:
            compDatos = c.split(",")
            componente = Componente(compDatos[0],compDatos[1],compDatos[2],compDatos[3])
            listaFinal.append(componente)
        productos.append(Producto(datos[0],datos[1],listaFinal))
    return productos


def xxx():
    os.system("cls")
    visuCsvComponentes()
    
xxx()