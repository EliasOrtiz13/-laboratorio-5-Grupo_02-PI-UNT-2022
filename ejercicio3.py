N = int(input('Ingrese el número de alumnos: '))
x=1
nom_alumnos = []
prom_alumnos = []

print ('Ingrese el nombre del alumno y su promedio')
while x <= N:
    N 
    nom = input ('Nombre del alumno: ')
    prom = int(input ('Promedio de {} es: '.format(nom)))

    nom_alumnos.append(nom)
    prom_alumnos.append(prom) 
    x+=1

def ordenamiento_inserción (a,b,c):
    for i in range (1,c):
        promedio = a[i]
        alumnos = b[i]
        j = i-1

        while (j>=0 and a[j]> promedio):
            a[j+1] = a[j]
            b[j+1] = b[j]
            j = j-1
            
            a[j+1] = promedio
            b[j+1] =alumnos

ordenamiento_inserción (prom_alumnos, nom_alumnos, N) 
print('Los promedios ordenados de menor a mayor son:')  
for k in range (N):
    print(nom_alumnos[k], prom_alumnos[k],sep=' --->> ' )