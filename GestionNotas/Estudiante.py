## Generar una clase Estudiante
class Estudiante:

    ## Constructor
    def __init__(self,nombre,edad,sistemasNota,programacionNota,baseDatosNota,redesNota):
        self.nombre = nombre
        self.edad = edad
        self.sistemasNota = sistemasNota
        self.programacionNota = programacionNota
        self.baseDatosNota = baseDatosNota
        self.redesNota = redesNota

    ## Está funcion es para poder mostrar por pantalla los datos
    def __str__(self):
        return self.nombre + " " + self.edad + " " + self.nota

    def media(self):
        media = (self.sistemasNota + self.programacionNota + self.baseDatosNota + self.redesNota)/2
        return media