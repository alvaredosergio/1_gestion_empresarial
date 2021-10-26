class Cliente:
    def __init__(self, id, nombre, meses,region):
        self.id = id
        self.nombre = nombre
        self.meses = meses
        self.region = region

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.notas)

    def toCSV(self):
        return self.nombre + ";" + str(self.edad) + ";" + str(self.notas["programacion"]) + str(
            self.notas["basedatos"]) + str(self.notas["redes"]) + str(self.notas["sistemas"])