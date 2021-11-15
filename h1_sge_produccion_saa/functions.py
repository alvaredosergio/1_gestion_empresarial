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
    print("| 1 - Productos \t|\n| 2 - Componentes \t|\n|\t\t\t|\n| 0 - Atrás \t\t|")
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
            componente = Componente(compDatos[0],int(compDatos[1]),compDatos[2],compDatos[3])
            listaFinal.append(componente)
        productos.append(Producto(datos[0],datos[1],listaFinal))
    return productos

## VISUALIZAR COMPONENTES
def visuCsvComponentes():
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
    return componentes

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
    while True:
        nombre = input("NOMBRE: ")
        costo = input("COSTO: ")
        categoria = input("CATEGORIA: ")
        proveedor = input("PROVEEDOR: ")
        crearComponente(Componente(nombre,costo,categoria,proveedor))
        sel = input("¿Desea introducir otro componente? (S/N)")
        if sel.lower() == "n":
            break
    return Componente(nombre,costo,categoria,proveedor)

## FUNCIÓN 1, PRESUPUESTO TOTAL NECESARIO PARA LA PRODUCCION DE ESE MES
def presuTotal():
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    suma0 = 0
    suma1 = 0
    suma2 = 0
    suma3 = 0
    total = 0
    for p in visuCsvProductos():
        x = int(p.prodMen)
        y0 = int(p.componentes[0].costo)
        y1 = int(p.componentes[1].costo)
        y2 = int(p.componentes[2].costo)
        y3 = int(p.componentes[3].costo)
        lista1.append(x*y0)
        lista2.append(x*y1)
        lista3.append(x*y2)
        lista4.append(x*y3)
    for l in lista1:
        suma0 += l
    for l in lista2:
        suma1 += l
    for l in lista3:
        suma2 += l
    for l in lista4:
        suma3 += l
    total = suma0 + suma1 + suma2 + suma3
    return total
    
## FUNCIÓN 2, PRESUPUESTO TOTAL POR PROVEEDOR
def presProveedor():
    asus = []
    corsair = []
    intel = []
    msi = []
    pbell = []
    totalPrAsus = 0
    totalPrCorsair = 0
    totalPrIntel = 0
    totalPrMsi = 0
    totalPrPbell = 0
    for c in visuCsvComponentes():
        if (c.proveedor == "ASUS"):
            asus.append(c)
        elif(c.proveedor == "Corsair"):
            corsair.append(c)
        elif(c.proveedor == "Intel"):
            intel.append(c)
        elif(c.proveedor == "MSI"):
            msi.append(c)
        elif(c.proveedor == "PBell"):
            pbell.append(c)

    print("Presupuesto unitario de cada Producto, por PROVEEDOR: ")
    print("-----------------------------------------------------")
    for a in asus:
        totalPrAsus += a.costo
    print("ASUS: \t\t" + str(totalPrAsus) + " €")
    for c in corsair:
        totalPrCorsair += a.costo
    print("Corsair: \t" + str(totalPrCorsair) + " €")
    for a in intel:
        totalPrIntel += a.costo
    print("Intel: \t\t" + str(totalPrIntel) + " €")
    for a in msi:
        totalPrMsi += a.costo
    print("MSI: \t\t" + str(totalPrMsi) + " €")
    for a in pbell:
        totalPrPbell += a.costo
    print("PBell: \t\t" + str(totalPrPbell) + " €")

## FUNCIÓN 3, DADO UN PRESUPUESTO ANUAL, SI LOS COSTOS SE VAN A EXCEDER
def calcularExcedentes(n):
    anual = presuTotal()*12
    if n < anual:
        print("Los costes actuales de " + str(anual) + "€/anual se van a exceder de lo planeado, " + str(n) + "€")
        print("DEBEMOS AJUSTAR PRESUPUESTOS.")
    else:
        print("Los costes actuales de " + str(anual) + "€/anual no se excederan de lo planeado, " + str(n) + "€")
        print("BUEN TRABAJO, SEGUIMOS ASÍ.")


