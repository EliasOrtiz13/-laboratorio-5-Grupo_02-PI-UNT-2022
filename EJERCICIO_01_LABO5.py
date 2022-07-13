n_nulos=0
p_posi=1
s_nega=0
i=0

n=int(input("Ingrese la cantidad de números que almacenará el conjunto: "))
conj=[]

print("Ingrese los valores del conjunto")
while i<n:
  conj.append(input())
  i += 1
i=0
while i<n:
  if int(conj[i])<0 :
    s_nega=s_nega+int(conj[i])
  
  if int(conj[i])>0 :
    p_posi=p_posi*int(conj[i])
  
  if int(conj[i])==0 :
    n_nulos=n_nulos+1
  
  i += 1

porcent_nu=n_nulos*100/n

print("La sumatoria de valores negativos del conjunto es: "+str(s_nega))
print("La productoria de valores positivos del conjunto es: "+ str(p_posi))
print("El porcentaje de valores nulos del conjunto es: "+str(porcent_nu)+" %")