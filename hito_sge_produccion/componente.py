class Componente:
    def __init__(self,nombre,costo:float,categoria,proveedor):
        self.nombre = nombre
        self.costo = costo
        self.categoria = categoria
        self.proveedor = proveedor

    def toList(self):
        todoComp = "[" + self.nombre + "," + self.costo + "," + self.categoria + "," + self.proveedor + "]"
        return todoComp

    def __str__(self):
        return self.nombre + "\t" + str(self.costo) + "€\t\t" + self.categoria + "\t\t" + self.proveedor
    
    def toCSV(self):
        return self.nombre + ";" + self.costo + ";" + self.categoria + ";" + self.proveedor + "\n"