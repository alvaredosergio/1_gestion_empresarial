class Producto:
    def __init__(self, nombre,prodMen,componente):
        self.nombre = nombre
        self.prodMen = prodMen
        self.componente = componente

    #def toList():
    #    return ",".join(self.componente)

    def __str__(self):
        return self.nombre + "\t\t" + self.prodMen + "\t\t" + self.componente #self.toList()

    def toCSV(self):
        return self.nombre + ";" + self.prodMen + ";" + self.componente #self.toList()

        