from Estudiante import *

## Creamos un fichero que abre el .csv que tenemos
fichero = open("grupo1.csv","r")

## Lee la primera linea del archivo .csv
linea = fichero.readline()

## Separa los datos de la primera linea por ;
headers = linea

## Leemos la siguiente linea
linea = fichero.readline()

## Lista de estudiantes
estudiantes = []

## Mientras la lista no este vacia:
while linea != '':
    datos = linea.split(";")

    print(datos)

    est = Estudiante(datos[0],int(datos[1]),notas(float(datos[2]),float(datos[3]),float(datos[4]),float(datos[5])))
    estudiantes.append(est)
    linea = fichero.readline()

## Cerramos el fichero para que guarde cambios
fichero.close()

## Añadimos un estudiante mas
estudiantes.append(Estudiante("Juan", 24,notas(5,6,7,8)))

## Bucle para mostrar la lista estudiantes
for est in estudiantes:
    print(est)

fichero = open("grupo2.csv","w")
fichero.write(headers)

for est in estudiantes:
    fichero.write(est.toCSV() + "\n")
fichero.close()

