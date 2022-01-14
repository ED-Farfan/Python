import math as m1
from random import randint
def binario(num):
    l = []
    nu = num

    while(nu != 0):
        l.append(nu%2==1)
        nu = nu // 2
    
    return l[: : -1]

def Exponenciacion(x,a,n):
    gio=""
    for i in range(30):
        gio += "-" 
    print(gio)
    print("Algoritmo de Exponenciacion")
    print(" x:"+str(x)+"\ta:"+str(a)+"\tn:"+str(n)+"\n")
    text = ""
    
    z = 1
    l = binario(a)
    for i in l:
        text += str(int(i))
    print("a_Bin: "+text+"\n")
    for i in l:
        z = (z**2)%n        
        z =  (z*x)%n if(i) else z
        print("-> a: "+str(int(i))+" z: "+str(z))
    print(gio)

    return z

def Algoritmo_Primalidad(num,veces=0,l=[]):    
    tex = str(num)
    if(tex[-1] in ['1','3','7','9']):
        n = num
        n_1 = n-1
        m = int(n_1 / 2)
        while not(str(m)[-1] in ['1','3','7','9']):
            m = int(m / 2)
        k = int(m1.log2(n_1/m))
        r=[]
        if(l==[]):            
            if(veces==0):
                aux = 0
                while(aux < k):
                    p = randint(1,n_1)                
                    if(not(p in l)):
                        l.append(p)
                        aux += 1
            else:
                for i in range(veces):
                    p = randint(1,n_1)
                    if(not(p in l)):
                        l.append(p)
        for a in l:
            r.append(Exponenciacion(a,m,n))
        return l[:],r[:],m,n,k

    else:
        return -1
def Resultados_Primalidad(r,l,m,n,k):
    gio=""
    for i in range(20):
        gio += "-" 
    print(gio)
    print("Algoritmo de Primalidad\n")
    print("n = "+str(n)+" n-1 = "+str(n-1)+" m = "+str(m)+ " k = "+str(k)+"\n")    
    for i in range(len(r)):
        print("["+str(l[i])+"^("+str(m)+")] mod "+str(n)+" = "+str(r[i]))
    if(1 in r):
        print("\n\t->Numero primo")
    else:
        print("\n\t->Numero compuesto")
    print(gio)

#hh = [10944102155,29942538789,10719745053,20778285603,14181972364,40626212286,25602805340,39285858419,26906853067,184345913]
l,r,m,n,k=Algoritmo_Primalidad(4331,10)
Resultados_Primalidad(r,l,m,n,k)

    