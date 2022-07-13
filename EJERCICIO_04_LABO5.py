t0=0
t1=1
t2=1
i=0
print("Ingresar el parámetro <n> para que se devuelva el <n+4> ésimo término")
n=int(input())
while i<=n :
    tn4=t0+t1+t2
    t0=t1
    t1=t2
    t2=tn4
    i +=1
print("El término del lugar " + str(n+4)+ " es "+str(tn4))