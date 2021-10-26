def calculo(unidad,precio):
    if unidad > 100:
        preciofinal = (precio * 0.9) * unidad
        print(round(preciofinal,2))
    print(round(unidad * precio,2))

calculo(15,56.458)


texto = "Este es el texto"
caracteres = len(texto)
print(caracteres)

textoInvertido = texto[::-1]
print(textoInvertido)

def bisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        print("El año " + str(anio) + " es bisiesto.")
    else:
        print("El año " + str(anio) + " NO es bisiesto.")

bisiesto(1976)


