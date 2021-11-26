class Empleado:

    def __init__(self,nombre,apellido,id,horas,salario):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.horas = horas
        self.salario = salario

    def __str__(self):
        return self.nombre + "\t\t" + self.apellido + "\t" + self.id + "\t\t" + self.horas + "\t\t" + self.salario + "€"

    def toCSV(self):
        return self.nombre + ";" + self.apellido + ";" + self.id + ";" + self.horas + ";" + self.salario + "\n"
