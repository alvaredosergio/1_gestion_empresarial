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

                    print("\n_______________________________________________________________________________\n0. Atrás")
            elif inp01 == 2:
                visuCsvComponentes()
                print("\n__________________________________________________________\n0. Atrás")
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
                print("f.1")
            elif inp01 == 2:
                print("f.2")
            elif inp01 == 3:
                print("f.3")
            elif inp01 == 0:
                break
    elif inp == 0:
        print("Usted salió del programa. Hasta pronto =)")
        break