def Convertir_Binario_Int(binario):
    C_Bin = binario[::-1]
    r=0
    for i in range(len(C_Bin)):
        r += (2**i)*int(C_Bin[i])
    return r
def Corrimiento_Izquierda(binario,veces,Ciclo = True):
    if(Ciclo):
        aux = binario[:]
        return aux[veces:]+aux[:veces]
    else:
        return [0]*(len(aux)-veces) + aux[:len(aux)-veces]
def Corrimiento_Derecha(binario,veces,Ciclo = True):
    if(Ciclo):
        aux = binario[:]
        return aux[len(aux)-veces:] + aux[:len(aux)-veces]
    else:
        return [0]*(len(aux)-veces) + aux[:len(aux)-veces]
def Cambiar_Cadena(binario, mascara):
    u = []
    m=[]
    for i in range(len(mascara)):
        u.append(binario[mascara[i]-1])
        m.append(mascara[i])
    return u[:],m[:]
    
def guardar_binario(binario,nombre,cad=[]):
    if(cad == []):
        Text =""
        Text0 = ""
        for i in range(0,len(binario)):        
            if(i%4 == 0):
                Text += '\t'+'--'+ '\t'+binario[i]
                Text0 += '\t'+'--'+'\t'+str(i+1)
            else:
                Text += '\t'+binario[i]
                Text0 += '\t'+str(i+1)
        Text = Text0 + '\n'+Text 
    else:
        Text =""
        Text0 = ""
        print(len(binario))
        for i in range(0,len(binario)):                    
            if(i%4 == 0):
                Text += '\t'+'--'+ '\t'+binario[i]
                Text0 += '\t'+'--'+'\t'+str(cad[i])
            else:
                Text += '\t'+binario[i]
                Text0 += '\t'+str(cad[i])
        Text = Text0 + '\n'+Text 
    archivo = open(nombre+".txt", 'w') # abre el archivo datos.txt    
    archivo.write(Text)
    archivo.close()
def Convertir_Hex_a_Int(numero):
    return int( numero, 16)
def Convertir_Int_a_Bin(numero):
    u=bin(numero)
    u = u[2:].split(maxsplit=len(u))
    print(len(u[0]))
    real=str(u[0])        
    return real
def LeerTabla(nombre):
    archivo = open(nombre+".txt", 'r') # abre el archivo datos.txt    
    A=archivo.readlines()
    archivo.close()    
    B = []
    for i in A:
        B.append(int(i[:len(i)-1]))
    return B
entero = Convertir_Hex_a_Int("a10f4708c621be73")
Bin = Convertir_Int_a_Bin(entero)
print(Bin)
print(len(Bin))
guardar_binario(Bin,"binario")
B = LeerTabla("Matriz_P1")
print(B)
n,m=Cambiar_Cadena(Bin,B)
guardar_binario(n,"PC_1",m)

C = n[:len(n)//2] # Izquierdo
D = n[len(n)//2:] # Derecho

C0 = m[:len(n)//2] # Izquierdo
D0 = m[len(n)//2:] # Derecho
C = Corrimiento_Izquierda(C,1)
D = Corrimiento_Izquierda(D,1)
C0 = Corrimiento_Izquierda(C0,1)
D0 = Corrimiento_Izquierda(D0,1)

guardar_binario(C,"Izq_1")
guardar_binario(D,"Derq_1")
guardar_binario(C+D,"C1D1")
B2 = LeerTabla("PC_2")
T = C0+D0
LLL = []
for i in range(len(T)):
    LLL.append([T[i],i+1])
    print("\n"+str(i+1)+"->"+str(T[i]))
print(len(T))
print("\n")
print(LLL)
print("\n")
n,m=Cambiar_Cadena(C+D,B2)
print(n)
print(m)
guardar_binario(n,"PC_22",m)
print("".join(n))
print(Convertir_Binario_Int(n))
print(hex(Convertir_Binario_Int(n)))

#n,m=Cambiar_Cadena(C+D,B2)
#guardar_binario(n,"PC_2CD",m)