from functions import *
from empleado import *
import os

while True:
    menuInicial()
    inp = checkearInt(input())
    if inp == 1:
        while True:
            os.system("cls")
            print("NOMBRE\t\tAPELLIDO\tIDENTIF.\tHORAS\t\tSALARIO")
            for e in visuEmpleados():
                print(e)
            print("________\n0. Atrás")
            inp01 = checkearInt(input())
            if inp01 == 0:
                break
            else:
                break
    elif inp == 2:
        while True:
            os.system ("cls")
            
            print("________\n0. Atrás")
    elif inp == 0:
        print("Usted salió del programa. Hasta pronto =)")
        break

