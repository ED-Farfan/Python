import math as m1
from random import randint

def binario(num=0):
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
def Euclides(r0,r1):
    q=[]
    r=[r0,r1]    
    while(r[-2]%r[-1] != 0 ):
        q.append((r[-2]-r[-2]%r[-1])//r[-1])
        r.append(r[-2]%r[-1])
    q.append((r[-2]-r[-2]%r[-1])//r[-1])
    return q,r
def Invertir(q,r):
    t=[0,1]
    for i in range(1,len(r)-1):
        t.append((t[i-1]-t[i]*q[i-1])%r[0])    
    return t
def Valor_Primo_Relativo(num):
    Ap = []
    for i in range(num):
        a=randint(2,num-1)
        q,r = Euclides(a,num)
        if(r[-1]==1 and not(a in Ap)):
            Ap.append(a)
    while(len(Ap)<2):
        a=randint(2,num-1)
        q,r = Euclides(a,num)
        if(r[-1]==1 and not(a in Ap)):
            Ap.append(a)
    Ap = sorted(Ap)    
    a=randint(0,len(Ap)-1)
    b=a
    while(b==a):
        b = randint(0,len(Ap)-1)    
    return Ap[a],Ap[b]
def Valor_Publico(phi,a):
    candidatos = []
    for i in range(phi):
        al = randint(1,phi)
        if((a*al)%phi == 1 and not(al in candidatos)):
            candidatos.append(al)
    
    while(len(candidatos)<1):
        al = randint(1,phi)
        if((a*al)%phi == 1  and not(al in candidatos)):
            candidatos.append(al)

    v = randint(0,len(candidatos)-1)
    
    return candidatos[v]
def Invertir(q,r):
    t=[0,1]
    for i in range(1,len(r)-1):
        t.append((t[i-1]-t[i]*q[i-1])%r[0])    
    return t
def resutadosE(q,r):
    print("\n")
    gio=""
    for i in range(20):
        gio+="-*-*"
    print(gio)
    print("\n\tAlgoritmo de Euclides\n")
    for i in range(1,len(r)-1):
        print("r["+str(i-1)+"]: "+str(r[i-1])+" = q["+str(i)+"] :"+str(q[i-1])+" x r["+str(i)+"]: "+str(r[i])+" + r["+str(i+1)+"]: "+str(r[i+1]))
    print("r["+str(len(r)-2)+"]: "+str(r[-1])+" = q["+str(len(q))+"] :"+str(q[-1])+" x r["+str(len(r)-1)+"]: "+str(r[-1])+" + 0")
    print("\nMCD("+str(r[0])+","+str(r[1]) +") = "+str(r[-1]))
    t = [0]
    if(q != [] and r[-1]==1):
        print("\nTiene inverso")
        t = Invertir(q,r)
        print("Inverso igual a "+str(t[-1]))               
    else:
        print("\nNo tiene inverso")
    
    print(gio)
    return t[-1]

def Calcular_LLaves(p,q,a=0):
    qq,r = Euclides(p,q)    
    if(r[-1]==1): #Son primos relativos
        phi = (p-1)*(q-1)
        if(a==0):
            a,f=Valor_Primo_Relativo(phi)
        qq,r = Euclides(phi,a)
        b = resutadosE(qq,r)
        print("\nRESULTATOS DE RSA LLAVES")        
        print("\n")
        text = "q: "+str(q)
        text += " p: "+str(p)
        text += " n: "+str(p*q)
        text += " phi(n): "+str(phi)
        text += "\n\n\tLlave privada[a]: "+str(a)+ " LLave publica[b]: "+str(b)
        print(text+"\n")
        return a,b,p*q
def encriptar(a,n,x):
    print("\n\n Algoritmo de encriptacion")
    y=Exponenciacion(x,a,n)
    print("\n\n")
    print("-> texto [x]:"+str(x)+" texto encriptado [y]: "+str(y))
    return y

def desencriptar(b,n,y):
    print("\n\n Algoritmo de Descifrado")
    x=Exponenciacion(y,b,n)
    print("\n\n")
    print("-> texto encriptado [y]:"+str(y)+" texto [x]: "+str(x))
    return x

def Encontrar_Llaves(p,q,aa=0,ab=0):
    gion = "|-|"
    for i in range(20):
        gion+="|-|"
    print("\n"+gion)
    print("\n\t ALGORITMO PARA ENCONTRAR LLAVES")
    if(aa!=0):
        aa,ba,n=Calcular_LLaves(p,q,aa)
        ab,bb,n=Calcular_LLaves(p,q,ab)
    else:
        aa,ba,n=Calcular_LLaves(p,q)
        ab,bb,n=Calcular_LLaves(p,q)
    print("\nRESULTADOS DE LLAVES")
    print("->Llave privada [a_A]: "+str(aa)+" Llave publica [b_A]: "+str(ba))
    print("->Llave privada [a_B]: "+str(ab)+" Llave publica [b_B]: "+str(bb))
    print("\n"+gion)
    return aa,ab,ba,bb,n
def Firmar(m,a,n,nombre=""):
    gion = "🔏"
    for i in range(20):
        gion+="🔏"
    print("\n"+gion)
    print("\n\t ALGORITMO PARA FIRMA DIGITAL")
    F=Exponenciacion(m,a,n)
    print("\nResultados de la firma")
    print("\n->Mensaje despues de HasSha: "+str(m)+" ->Firmando con llave privada: "+str(F)+" ->Llave privada: "+str(a)+" ->Le pertenece : "+str(nombre))
    print("\n"+gion)
    
    return F
def Comprobar_Firma(F,b,n,m,nombre=""):
    gion = "🧐"
    for i in range(20):
        gion+="🧐"
    print("\n"+gion)
    print("\n\t ALGORITMO PARA COMPROBAR FIRMA DIGITAL")
    h=Exponenciacion(F,b,n)
    print("\nResultados de la comprobacion de la firma")
    print("\n->Mensaje despues de HasSha: "+str(m)+" ->Firmando con llave privada: "+str(F)+" ->Llave publica: "+str(b)+" ->Hasha de mensaje recivido: "+str(h)+" ->Lo Recibe: "+str(nombre))
    if(h == m):
        print("\nSe acepta la firma")
    else:
        print("\nSe rechaza la firma")
    print("\n"+gion)
    return m




#a,b=Valor_Primo_Relativo(32040)
#print(a)
#print(b)
#print(Valor_Publico(32040,22223))
####
#a,b,n=Calcular_LLaves(181,179,22223)
#y=encriptar(a,n,512)
#x=desencriptar(b,n,y)
######
#aa,ab=Valor_Primo_Relativo(32040)
#aa = 23881
#ab = 17573
#print(aa,ab)
#ba =Valor_Publico(32040,aa)
#bb =Valor_Publico(32040,ab)
#print(ba,bb)
#print(Exponenciacion(53,23881,32040))
#h_1=pow(53,23881,32040)
#print(pow(h_1,30481,32040))
######
#a = 31
#phi = 42593
#q,r=Euclides(phi,a)
#t=Invertir(q,r)
#b = t
#print(b)
#h_1 = pow(53,a,phi)
#h = pow(h_1,b,phi)
#print(h_1,h)
##########################################
aa,ab,ba,bb,n=Encontrar_Llaves(181,179,23881,17573)
F=Firmar(53,aa,n,"A")
Comprobar_Firma(F,ba,n,53,"B")