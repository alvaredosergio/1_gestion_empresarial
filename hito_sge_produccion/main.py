import os
from functions import *
from producto import *
from componente import *

menuInicial()
inp01 = int(input())
if inp01 == 1:
    menuVisualizar()
    inp02 = int(input())
    if inp02 == 1:
        visuCsvProductos()
    elif inp02 == 2:
        visuCsvComponentes()
    else:
        print("Error en introducción. Pruebe de nuevo")
elif inp01 == 2:
    menuCrear()
    inp03 = int(input())
    if inp03 == 1:
        os.system ("cls")
        nombre = input("NOMBRE: ")
        prodMen = input("PROD. MENSUAL: ")
        componente = input("COMPONENTE: ")
        '''componentes = []
        while True:
            comp = input("Introduce un componente: ")
            componentes.append(comp)
            sel = input("¿Quieres introducir otro componente? (S/N)")
            if sel != 'S':
                break'''
        crearProducto(nombre,prodMen,componente)
    elif inp03 == 2:
        os.system ("cls")
        nombre = input("NOMBRE: ")
        costo = input("COSTO: ")
        categoria = input("CATEGORIA: ")
        proveedor = input("PROVEEDOR: ")
        crearComponente(nombre,costo,categoria,proveedor)
    else:
        print("Error en introducción. Pruebe de nuevo")
elif inp01 == 3:
    menuExtra()
elif inp01 == 0:
    print("Usted salió del programa. Hasta pronto =)")
else:
    print("Error en introducción. Pruebe de nuevo.")