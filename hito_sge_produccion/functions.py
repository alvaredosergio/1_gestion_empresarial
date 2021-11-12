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
def crearProducto(producto:Producto):
    nuevoRegistro = producto.toCSV()
    file = open('csv/productos.csv', 'a')
    file.write(nuevoRegistro)
    file.close

## CREAR COMPONENTE
def crearComponente(componente:Componente):
    nuevoRegistro = componente.toCSV()
    file = open('csv/componentes.csv', 'a')
    file.write(nuevoRegistro)
    file.close

## CHECKEAR INTEGER
def checkearInt(inp):
    try:
        inp = int(inp)
    except:
        return -1
    return inp

## INTRODUCIR PRODUCTO
def introProdu():
    nombre = input("NOMBRE: ")
    prodMen = input("PROD. MENSUAL: ")
    componentes = []
    print("Vas a introducir los componentes: ")
    x = 1   
    while True:
        print("Introduce el componente número " + str(x))
        comp = introComp()
        componentes.append(comp)
        x += 1
        sel = input("¿Desea introducir otro componente? (S/N)")
        if sel.lower() == "n":
            break
    return Producto(nombre,prodMen,componentes)
## INTRODUCIR COMPONENTE
def introComp():
    nombre = input("NOMBRE: ")
    costo = input("COSTO: ")
    categoria = input("CATEGORIA: ")
    proveedor = input("PROVEEDOR: ")
    crearComponente(Componente(nombre,costo,categoria,proveedor))
    return Componente(nombre,costo,categoria,proveedor)

## FUNCIÓN 1, PRESUPUESTO TOTAL NECESARIO PARA LA PRODUCCION DE ESE MES
def presupMes():
    visuCsvProductos()
    return

## FUNCIÓN 2, PRESUPUESTO TOTAL POR PROVEEDOR
def presupProv():
    return

## FUNCIÓN 3, DADO UN PRESUPUESTO ANUAL, SI LOS COSTOS SE VAN A EXCEDER
def calcularExcedentes():
    return


