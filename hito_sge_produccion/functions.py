import os
from producto import Producto
from componente import Componente

## MENU INICIAL
def menuInicial():
    os.system ("cls")
    print("Bienvenido al GESTOR DE PRODUCCIÓN.")
    print("¿Qué desea realizar?\n-------------------------")
    print("| 1 - Visualizar CSV \t|\n| 2 - Crear registro \t|\n| 3 - Opciones extras \t|\n|\t\t\t|\n| 0 - Salir \t\t|")
    print("-------------------------")

## MENU VISUALIZAR
def menuVisualizar():
    os.system ("cls")
    print("¿Qué CSV desea visualizar?\n-------------------------")
    print("| 1 - Productos \t|\n| 2 - Consumibles \t|\n|\t\t\t|\n| 0 - Atrás \t\t|")
    print("-------------------------")

## MENU CREAR REGISTRO
def menuCrear():
    os.system ("cls")
    print("¿Qué CSV desea utilizar?\n-------------------------")
    print("| 1 - Productos \t|\n| 2 - Componentes \t|\n|\t\t\t|\n| 0 - Atrás \t\t|")
    print("-------------------------")

## MENU EXTRA
def menuExtra():
    os.system ("cls")
    print("¿Qué función desea utilizar?\n-----------------------------------------")
    print("| 1 - Presupuesto de producción mensual |\n| 2 - Presupuesto por proveedor \t|\n| 3 - Excedente de costos \t\t|\n|\t\t\t\t\t|\n| 0 - Atrás \t\t\t\t|")
    print("-----------------------------------------")

## VISUALIZAR PRODUCTOS
def visuCsvProductos():
    os.system ("cls")
    file = open("csv/productos.csv",'r')
    header = file.readline()
    productos = []
    line = file.readline()
    while line != "":
        lineaBuena = line.split("\n")[0]
        datos = lineaBuena.split(";")
        pr = Producto(datos[0],datos[1],datos[2])
        productos.append(pr)
        line = file.readline()
    file.close()
    print("NOMBRE\t\tPRD.MENSUAL\tCOMPONENTES")
    for prod in productos:
        print(prod)

## VISUALIZAR COMPONENTES
def visuCsvComponentes():
    os.system ("cls")
    file = open("csv/componentes.csv",'r')
    header = file.readline()
    componentes = []
    line = file.readline()
    while line != "":
        lineaBuena = line.split("\n")[0]
        datos = lineaBuena.split(";")
        co = Componente(datos[0],float(datos[1]),datos[2],datos[3])
        componentes.append(co)
        line = file.readline()
    file.close()
    print("NOMBRE\t\tCOSTO\t\tCATEGORIA\tPROVEEDOR")
    for com in componentes:
        print(com)

## CREAR PRODUCTO
def crearProducto(nombre,prodMen,componente):
    nuevoRegistro = nombre + ";" + prodMen + ";" + componente + "\n"
    file = open('csv/productos.csv', 'a')
    file.write(nuevoRegistro)
    file.close

## CREAR COMPONENTE
def crearComponente(nombre,costo,categoria,proveedor):
    nuevoRegistro = nombre + ";" + costo + ";" + categoria + ";" + proveedor + "\n"
    file = open('csv/componentes.csv', 'a')
    file.write(nuevoRegistro)
    file.close

    



        