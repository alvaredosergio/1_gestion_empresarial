## Generar una funcion con una libreria
def avion(numero, pasajeros, tipo, aerolinea):
    return {"num": numero, "pas": pasajeros, "tip": tipo, "aer": aerolinea}

## Generar una clase Avion
class Avion:

    ## Constructor
    def __init__(self,numero,pasajeros,tipo,aerolinea):
        self.numero = numero
        self.pasajeros = pasajeros
        self.tipo = tipo
        self.aerolinea = aerolinea

    ## Está funcion es para poder mostrar por pantalla los datos
    def __str__(self):
        return self.numero + " " + str(self.pasajeros) + " " + self.tipo + " " + self.aerolinea
