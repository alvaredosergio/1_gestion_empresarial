## Diccionario NOTAS
def notas(np,nbd,nr,ns):
    return {"programacion":np, "basedatos":nbd, "redes":nr, "sistemas":ns}

## Clase Estudiante
class Estudiante:
    def __init__(self,nombre,edad,notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.notas)

    def toCSV(self):
        return self.nombre + ";" + str(self.edad) + ";" + str(self.notas["programacion"]) + str(self.notas["basedatos"]) + str(self.notas["redes"]) + str(self.notas["sistemas"])

