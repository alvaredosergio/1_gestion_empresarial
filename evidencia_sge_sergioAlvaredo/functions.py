from empleado import *
import os

def nuevoTrabajador(empleado:Empleado):
    nuevoRegistro = empleado.toCSV()
    file = open('empleados.csv', 'a')
    file.write(nuevoRegistro)
    file.close

def visuEmpleados():
    file = open("empleados.csv",'r')
    header = file.readline()
    empleados = []
    line = file.readline()
    while line != "":
        lineaBuena = line.split("\n")[0]
        datos = lineaBuena.split(";")
        em = Empleado(datos[0],datos[1],datos[2],datos[3],datos[4])
        empleados.append(em)
        line = file.readline()
    file.close()
    return empleados

def checkearInt(inp):
    try:
        inp = int(inp)
    except:
        return -1
    return inp

def introEmp():
    while True:
        nombre = input("NOMBRE: ")
        costo = input("COSTO: ")
        categoria = input("CATEGORIA: ")
        proveedor = input("PROVEEDOR: ")
        (Componente(nombre,costo,categoria,proveedor))
        sel = input("¿Desea introducir otro componente? (S/N)")
        if sel.lower() == "n":
            break
    return Componente(nombre,costo,categoria,proveedor)


def menuInicial():
    os.system ("cls")
    print("Bienvenido al gestor de EMPLEADOS.")
    print("¿Qué desea realizar?\n-------------------------")
    print("| 1 - Ver empleados \t|\n| 2 - Crear empleado \t|\n| 3 - Opciones extras \t|\n|\t\t\t|\n| 0 - Salir \t\t|")
    print("-------------------------")