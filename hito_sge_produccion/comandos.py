import os
from producto import Producto
from consumible import Consumible

def comandoInicial():
    os.system ("cls")
    print("Bienvenido al Gestor de Producción.")
    print("¿Qué desea realizar?\n-------------------------")
    print("| 1 - Visualizar CSV \t|\n| 2 - Borrar CSV \t|\n| 3 - Modificar CSV \t|")
    print("-------------------------")
   
def priMenu(entrada):
    if entrada == "1":
        os.system ("cls")
        print("¿Qué CSV desea visualizar?\n-------------------------")
        print("| 1 - Productos \t|\n| 2 - Consumibles \t|")
        print("-------------------------")
    elif entrada == "2":
        os.system ("cls")
        print("Opción 2")
    elif entrada == "3":
        os.system ("cls")
        print("Opción 3")
    else:
        print("Opcción incorrecta. Intentelo de nuevo.")

def visuCsv(entrada):
    os.system ("cls")
    if entrada == "1":
        fichero = open("csv/productos.csv",'r')
        linea = fichero.readline()
        productos = []
        while linea != "":
            datos = linea.split(";")
            pr = Producto(datos[0],datos[1],datos[2])
            productos.append(pr)
            linea = fichero.readline()
        fichero.close()
        for prod in productos:
            print(prod)

    elif entrada == "2":
        fichero2 = open("csv/consumibles.csv",'r')
        linea = fichero2.readline()
        consumibles = []
        while linea != "":
            datos = linea.split(";")
            co = Consumible(datos[0],datos[1],datos[2],datos[3])
            consumibles.append(co)
            linea = fichero2.readline()
        fichero2.close()
        for cons in consumibles:
            print(cons)
    else:
        print("El csv no es correcto. Intentelo de nuevo.")

        