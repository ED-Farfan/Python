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
    print("\n [x: "+str(x)+"^(a: "+str(a)+")] mod n: "+str(n)+"= "+str(z)+"\n")
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

def numero_aleatorio_digitos(dig,term=-1):
    if(dig > 0):
        A=1
        r=0
        if(term == -1):
            for i in range(dig):
                r+= randint(0,9)*A
                A=A*10
        else:
            r+= [3,5,7,9][randint(0,3)]*A
            A = A*10
            for i in range(dig-1):
                r+= randint(0,9)*A
                A=A*10
            
        return r


#Exponenciacion(8724,2157,997)
#Exponenciacion(7259,9031,10009)
#print(pow(8724,2157,997))
#print(pow(7259,9031,10009))



#num=numero_aleatorio_digitos(11,1)
#num = 42209234693 
#l,r=Algoritmo_Primalidad(num,10)
#for  i in range(len(l)):
#    print(str(l[i])+"\t"+str(r[i]))
#x=1948428548103252553440910233292332574267708026374
#a=6831768736298356852765711232971351220781970451852      
#n=91979005674583198516719047677281136685024526413957

#print(Exponenciacion(x,a,n))
#print(pow(x,a,n))
x = 1999
b = 1936
n =  176347
Exponenciacion(x,b,n)
print(pow(x,b,n))
#y = Exponenciacion(x,b,n)
#a = 22223
#print(pow(x,a,n))
#print(Exponenciacion(y,a,n))

