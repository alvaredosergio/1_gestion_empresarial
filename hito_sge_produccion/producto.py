class Producto:
    def __init__(self, nombre,prodMen,componentes):
        self.nombre = nombre
        self.prodMen = prodMen
        self.componentes = componentes

    def __str__(self):
        return self.nombre + " " + self.prodMen + " " + self.componentes

    def toCSV(self):
        return self.nombre + ";" + self.prodMen + ";" + self.componentes + ";" 