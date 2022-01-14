import random
import numpy as np
def Arreglo_Pi_Y_Pi_1(tamanio):
    if(tamanio > 1 ):
        L = list(range(1,tamanio+1,1))
        LL = L[:]
        PI = [0]*tamanio
        PI_1 = [0]*tamanio
        while(len(L)>0):
            aleatorio =  random.choice(LL)
            if(aleatorio != L[0]):
                PI[aleatorio-1]=L.pop(0)
                PI_1[PI[aleatorio-1]-1]=aleatorio
                LL.remove(aleatorio)
            elif(len(L)==1):
                PI[aleatorio-1]=L.pop(0)
                PI_1[PI[aleatorio-1]-1]=aleatorio
                LL.remove(aleatorio)
        return PI,PI_1
    else:
        return [],[]
def Matrices_PI_y_PI_1(Pi,Pi_1,col,Fil):
    if(len(Pi)!=0):
        tam=int(len(Pi)**(1/2))
        Mat_Pi = np.array(Pi).reshape(Fil,col)
        Mat_PI_1 = np.array(Pi_1).reshape(Fil,col)
        return Mat_Pi,Mat_PI_1
    else:
        return [], []
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

Pi,PI=Arreglo_Pi_Y_Pi_1(96)
Mat_Pi,Mat_PI_1 = Matrices_PI_y_PI_1(Pi,PI,8,12)
print(Mat_Pi)
print(Mat_PI_1)
Guardar_Matriz("Matriz_PI",Mat_Pi)
Guardar_Matriz("Matriz_PI_1",Mat_PI_1)