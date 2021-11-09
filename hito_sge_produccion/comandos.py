import os
from producto import Producto
from componente import Componente
from csv import *

def comandoInicial():
        os.system ("cls")
        print("Bienvenido al GESTOR DE PRODUCCIÓN.")
        print("¿Qué desea realizar?\n-------------------------")
        print("| 1 - Visualizar CSV \t|\n| 2 - Crear registro \t|\n| 3 - Opciones extras \t|")
        print("-------------------------")
   
def priMenu(entrada):
    if entrada == "1":
        os.system ("cls")
        print("¿Qué CSV desea visualizar?\n-------------------------")
        print("| 1 - Productos \t|\n| 2 - Consumibles \t|")
        print("-------------------------")

    elif entrada == "2":
        os.system ("cls")
        print("¿Qué CSV desea utilizar?\n-------------------------")
        print("| 1 - Productos \t|\n| 2 - Componentes \t|")
        print("-------------------------")
        input04 = input()
        if input04 == "1":
            os.system ("cls")
            print("NOMBRE del producto: ")
            inp01 = input()
            print("PROD. MENSUAL del producto: ")
            inp02 = input()
            print("COMPONENTE del producto: ")
            inp03 = input()
            crearProducto(inp01,inp02,inp03)
        elif input04 == "2":
            os.system ("cls")
            print("NOMBRE del componente: ")
            inp01 = input()
            print("COSTE del producto /u: ")
            inp02 = input()
            print("CATEGORIA del producto: ")
            inp03 = input()
            print("PROVEEDOR: ")
            inp04 = input()
            crearComponente(inp01,inp02,inp03,inp04)
        else:
            print("Opción incorrecta. Intentelo de nuevo.")

    elif entrada == "3":
        os.system ("cls")
        print("¿Qué función desea utilizar?\n-----------------------------------------")
        print("| 1 - Presupuesto de producción mensual |\n| 2 - Presupuesto por proveedor \t|\n| 3 - Excedente de costos \t\t|")
        print("-----------------------------------------")
        
    else:
        print("Opcción incorrecta. Intentelo de nuevo.")

def visuCsv(entrada):
    os.system ("cls")
    if entrada == "1":
        fichero = open("csv/productos.csv",'r')
        linea = fichero.readline()

        productos = []
        while linea != "":
            lineaBuena = linea.split("\n")[0]
            datos = lineaBuena.split(";")
            pr = Producto(datos[0],datos[1],datos[2])
            productos.append(pr)
            linea = fichero.readline()
        fichero.close()
        for prod in productos:
            print(prod)

    elif entrada == "2":
        fichero2 = open("csv/componentes.csv",'r')
        linea = fichero2.readline()
        componentes = []
        while linea != "":
            lineaBuena = linea.split("\n")[0]
            datos = lineaBuena.split(";")
            co = Componente(datos[0],datos[1],datos[2],datos[3])
            componentes.append(co)
            linea = fichero2.readline()
        fichero2.close()
        for cons in componentes:
            print(cons)
    else:
        print("El csv no es correcto. Intentelo de nuevo.")

def crearProducto(nombre,prodMen,componente):
    nuevoRegistro = nombre + ";" + prodMen + ";" + componente + "\n"
    file = open('csv/productos.csv', 'a')
    file.write(nuevoRegistro)
    file.close

def crearComponente(nombre,costo,categoria,proveedor):
    nuevoRegistro = nombre + ";" + costo + ";" + categoria + ";" + proveedor + "\n"
    file = open('csv/componentes.csv', 'a')
    file.write(nuevoRegistro)
    file.close

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
    



        