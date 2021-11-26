from Avion import Avion

class Aeropuerto:
    def __init__(self):
        ## Creamos 3 listas para guardar los aviones
        self.tipoA = []
        self.tipoB = []
        self.tipoC = []

    ## Funcion para comprobar si la lista tipoA, que determina los aviones que hay en el aeropuerto,
    ## tiene espacio mas de 20 para añadir un avion
    def aterrizarAvion(self,avion):

        ## tipo 1 de if
        if avion.tipo == 'A':
            if len(self.tipoA) < 20:
                self.tipoA.append(avion)
                return True

        ## tipo 2 de if
        if avion.tipo == 'B' and len(self.tipoB) < 20:
            self.tipoB.append(avion)
            return self.tipoB

        if avion.tipo == 'C' and len(self.tipoC) < 20:
            self.tipoC.append(avion)
            return len(self.tipoC)
        return False

    ## Funcion para comprobar la capacidad de los aviones
    def capacidadAviones(self):
        sum = 0
        for avion in self.tipoA:
            sum = sum + avion.pasajeros

        for avion in self.tipoB:
            sum = sum + avion.pasajeros

        for avion in self.tipoC:
            sum = sum + avion.pasajeros
        return sum