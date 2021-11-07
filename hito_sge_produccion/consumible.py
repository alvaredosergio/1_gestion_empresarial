class Consumible:
    def __init__(self, nombre,costo,categoria,proveedor):
        self.nombre = nombre
        self.costo = costo
        self.categoria = categoria
        self.proveedor = proveedor

    def __str__(self):
        return self.nombre + " " + self.costo + " " + self.categoria + " " + self.proveedor

    def toCSV(self):
        return self.nombre + ";" + self.costo + ";" + self.categoria + ";" + self.proveedor + ";"