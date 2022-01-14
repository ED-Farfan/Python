import random
import numpy as np

def Guardar_Matriz(nombre,matriz):
    if(len(matriz)!=0):
        fil,col = matriz.shape
        Text=""
        for j in range(0,fil):
            for i in range(0,col):
                if(i==0):
                    Text += str(matriz[j,i])
                else:
                    Text += "\t" + str(matriz[j,i])
            Text += "\n"        
        archivo = open(nombre+".txt", 'w') # abre el archivo datos.txt
        archivo.write(Text)
        archivo.close()

def Crear_Matriz_S():
    lista = list(range(0,16))
    lista = lista
    listaR1 = []
    listaR2 = []
    listaR3 = []
    listaR4 = []
    while(len(lista)>0):
        dato = random.choice(lista)    
        lista.remove(dato)
        listaR1.append(dato)
    lista = list(range(0,16))
    i=0
    while(len(lista)>0):
        dato = random.choice(lista)    
        if(listaR1[i]!=dato):
            lista.remove(dato)
            listaR2.append(dato)
            i += 1
        elif(len(lista)==1):
            lista.remove(dato)
            listaR2.append(dato)
    lista = list(range(0,16))
    i = 0
    while(len(lista)>0):
        dato = random.choice(lista)    
        if(listaR1[i]!=dato and listaR2[i]!=dato):
            lista.remove(dato)
            listaR3.append(dato)
            i += 1
        elif(len(lista)==1):
            lista.remove(dato)
            listaR3.append(dato)
    lista = list(range(0,16))
    i = 0
    while(len(lista)>0):
        dato = random.choice(lista)    
        if(listaR1[i]!=dato and listaR2[i]!=dato and listaR3[i]!=dato):
            lista.remove(dato)
            listaR4.append(dato)
            i += 1
        elif(len(lista)==1):
            lista.remove(dato)
            listaR4.append(dato)
    listaR = listaR1 + listaR2 +listaR3+listaR4

    return np.array(listaR).reshape(4,16)
matriz=Crear_Matriz_S()
print(matriz)
Guardar_Matriz("Matriz_Box_S",matriz)