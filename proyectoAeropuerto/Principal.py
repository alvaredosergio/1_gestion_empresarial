from Aeropuerto import Aeropuerto
from Avion import Avion

## Instanciamos 3 aviones
a1 = Avion("A123",120,'A',"Iberia")
a2 = Avion("B456",200,'B',"Rayner")
a3 = Avion("C350",110,'C',"Fly Emirates")

## Instancioamos un aeropuerto vacio
aeropuerto = Aeropuerto()

## Ejecutamos la funcion aterrizarAvion y l pintamos en terminal
print(aeropuerto.aterrizarAvion(a1))
print(aeropuerto.aterrizarAvion(a2))
print(aeropuerto.aterrizarAvion(a3))

## Introducimos 20 aviones y vemos que nos retorna true hasta el avion 21 que nos retorna False
for i in range (20):
    print(aeropuerto.aterrizarAvion(a1))

## Funcion para mostrar capacidad de todos los aviones del aeropuerto
print(aeropuerto.capacidadAviones())