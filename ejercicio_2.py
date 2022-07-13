n=int(input("Ingrese el número de pares de valores X1 y X2: "))
listaNum1 = []
listaNum2 = []
for i in range(n):
    print("Ingrese el ", i+1,"° par de numeros enteros positivos: ")
    
    num1=int(input())
    while num1<=0:
        num1=int(input("El número ingresado no es entero positivo, ingrese de nuevo: "))
    listaNum1.append(num1)
    
    num2=int(input())
    while num2<=0:
        num2=int(input("El número ingresado no es entero positivo, ingrese de nuevo: "))
    listaNum2.append(num2)

# 1. Promedio de num1 y num2
listaPromedio = []
for i in range(n):
    promedio = (listaNum1[i] + listaNum2[i])/2
    listaPromedio.append(promedio)

# 2.  Media geométrica de num1 y num2
import math
listaMediaGeometrica = []
for i in range(n) :
    medGeometric = math.sqrt(listaNum1[i]*listaNum2[i])
    listaMediaGeometrica.append(medGeometric)

# 3. Porcentaje de veces que media geométrica es menor que promedio.
listaPorcentajeMGmenorMA = []
for i in range(n):
    porcentaje = 100 - (listaMediaGeometrica[i]/listaPromedio[i]) * 100
    listaPorcentajeMGmenorMA.append(porcentaje)

#Tabla de datos
print( """\
+-------------------------------------------------------------------+
|    X1     X2    Promedio    Media Geometrica    Porcentaje MG<P   |
|-------------------------------------------------------------------|""")
for i in range (n):
    a = print("| {0:>5} {1:>6} {2:>10} {3:>16.2f} {4:>17.2f}%       |".format(
   listaNum1[i], listaNum2[i], listaPromedio[i], listaMediaGeometrica[i], listaPorcentajeMGmenorMA[i]))
print("+-------------------------------------------------------------------+")

# 4. El primer par de valores donde: promedio igual a media geométrica.
listMedgeoIgualPromNum1 = []
listMedgeoIgualPromNum2 = []
for i in range(n):
    if listaPromedio[i] == listaMediaGeometrica[i]:
        listMedgeoIgualPromNum1.append(listaNum1[i])
        listMedgeoIgualPromNum2.append(listaNum2[i])

print("Primer par de valores donde el promedio es igual a la media geométrica:")
if len(listMedgeoIgualPromNum1) == 0 and len(listMedgeoIgualPromNum2) == 0 :
    print("No existe tal par de X1 y X2")
else :
    print("(", listMedgeoIgualPromNum1[0], ";", listMedgeoIgualPromNum2[0], ")")