from time import time
sumas=list(range(0,4))
resultados=[]
start_time = time()
for a in sumas:
    r=0
    if(a==0):
        for i in range(0,10000000):
            r += 4/(8*i+1)
    else:
        for i in range(0,10000000):
            r += 4/(8*i+2*(a-1)+3)
    resultados.append(r)
print(resultados)
for i in range(0,4):
    resultados[i]= resultados[i]if (i%2 == 0) else -1*resultados[i]

r=0
for i in resultados:
    r+=i    
print(r)
elapsed_time = time() - start_time
print("Tiempo de ejecucion: "+str(elapsed_time))
