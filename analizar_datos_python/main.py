from cliente import Cliente

fichero =open("datos ejemplo.csv",'r')
linea=fichero.readline()
clientes=[]
while linea!="":
    datos=linea.split(";")
    cl=Cliente(datos[0],datos[1],[float(datos[2]),float(datos[3]),float(datos[4]),float(datos[5])],datos[6])
    clientes.append(cl)
    linea=fichero.readline()
fichero.close()

print("Clientes con saldo negativo")
for cl in clientes:
    for mes in cl.meses:
        if mes<=-200:
            print(cl.nombre)
            break

fichero2=open("region.csv",'w')
regiones={}

for cl in clientes:
    for mes in cl.meses:
        if regiones.get(cl.region)==None:
            regiones[cl.region]=0
        regiones[cl.region]=regiones[cl.region]+mes

for key,value in regiones.items():
    print(key," <-> ", round(value,2))
    fichero2.write(str(key+";"+str(round(value,2)))+"\n")

fichero2.close()

max=sum(clientes[0].meses)
min=sum(clientes[0].meses)
maxCliente=clientes[0].nombre
minCliente=clientes[0].nombre
for cl in clientes:
   suma= sum(cl.meses)
   if max<suma:
       max=suma
       maxCliente=cl.nombre
   if min>suma:
       min=suma
       minCliente=cl.nombre
print("el cliente con mayor balance es ",maxCliente)
print("el cliente con menor balance es ",minCliente)

R=0

while R!=8:
    print("menu")
    print("8- Salir")
    R=int(input())