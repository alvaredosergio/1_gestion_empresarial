class Producto:
    def __init__(self, nombre,prodMen:int,componentes):
        self.nombre = nombre
        self.prodMen = prodMen
        self.componentes = componentes

    def listarComponentes(self):
        todoProd = "["
        x = 0
        for comp in self.componentes:
            todoProd += comp.toList()
            x += 1
            if x < len(self.componentes):
                todoProd += ","
        todoProd += "]"
        return todoProd

    def __str__(self):
        return self.nombre + "\t" + str(self.prodMen) + "\t\t" + self.listarComponentes()

    def toCSV(self):
        return self.nombre + ";" + str(self.prodMen) + ";" + self.listarComponentes() + "\n"

        