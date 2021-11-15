import os
from functions import *
from producto import *
from componente import *

while True:
    menuInicial()
    inp = checkearInt(input())
    if inp == 1:
        menuVisualizar()
        while True:
            inp01 = checkearInt(input())
            if inp01 == 1:
                os.system ("cls")
                print("NOMBRE\t\tPRD.MENSUAL\tCOMPONENTES")
                for p in visuCsvProductos():
                    print (p)
                print("________\n0. Atrás")
            elif inp01 == 2:
                os.system ("cls")
                print("NOMBRE\t\tCOSTO\t\tCATEGORIA\tPROVEEDOR")
                for com in visuCsvComponentes():
                    print(com)
                print("________\n0. Atrás")
            elif inp01 == 0:
                break
    elif inp == 2:
        while True:
            menuCrear()
            inp01 = checkearInt(input())
            if inp01 == 1:
                os.system ("cls")
                producto = introProdu()
                crearProducto(producto)
            elif inp01 == 2:
                os.system ("cls")
                componente = introComp()
            elif inp01 == 0:
                break
    elif inp == 3:
        menuExtra()
        while True:
            inp01 = checkearInt(input())
            if inp01 == 1:
                os.system ("cls")
                print("Presupuesto TOTAL de la producción mensual: ")
                print("-------------------------------------------")
                print(str(presuTotal()) + " €")
                print("________\n0. Atrás")
            elif inp01 == 2:
                os.system ("cls")
                presProveedor()
                print("________\n0. Atrás")
            elif inp01 == 3:
                os.system ("cls")
                inp31 = int(input("Escriba el presupuesto anual esperado:"))
                calcularExcedentes(inp31)
                print("________\n0. Atrás")
            elif inp01 == 0:
                break
    elif inp == 0:
        print("Usted salió del programa. Hasta pronto =)")
        break