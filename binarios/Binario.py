#https://www.youtube.com/watch?v=rVdysQGa-08
def Corrimiento_Derecha(binario,veces,Ciclo = True):
    if(Ciclo):
        aux = binario[:]
        return aux[len(aux)-veces:] + aux[:len(aux)-veces]
    else:
        return [0]*(len(aux)-veces) + aux[:len(aux)-veces]
def Incrementar_Bits(binario,bits):
    if(len(binario) < bits):
        return [0]*(bits-len(binario))+ binario        
    else:
        return binario

def Convertir_Int_Binario(numero,bits=0):
    B=[]
    div = numero
    while(div !=0):
        B.append(div%2)
        div = div//2
    if(len(B)<bits):
        B+=[0]*(bits-len(B))
    return B[::-1]

def Convertir_Binario_Int(binario):
    C_Bin = binario[::-1]
    r=0
    for i in range(len(C_Bin)):
        r += (2**i)*C_Bin[i]
    return r
U=Convertir_Int_Binario(63)

print(Incrementar_Bits(U,10))
for i in range(1):
    LL=Corrimiento_Derecha(U,i)
    print(Convertir_Binario_Int(LL))
    print(LL)
