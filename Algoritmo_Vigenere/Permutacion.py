import math
def CorrimientoDerecha(texto,corr):
    texto2=""
    texto2 = texto[len(texto)-corr : ] + texto[ : len(texto)-corr]
    return texto2
def CorrimientoIzquierda(texto,corr):   
    
    texto2=""    
    if(len(texto)%2 != 0):        
        texto2 = texto[len(texto)-corr+1  : ]+texto[ : len(texto)-corr+1]        
    else:
        texto2 = texto[len(texto)-corr  : ]+texto[ : len(texto)-corr]
    return texto2
def Encriptar(texto):    
    texto = CorrimientoDerecha(texto,math.ceil(math.log2(len(texto))))        
    aux = texto[1:len(texto)-1]    
    texto = texto[0]+aux[::-1]+texto[len(texto)-1]        
    mitad = len(texto)//2
    texto = texto[mitad:]+texto[:mitad]
    return texto

def Desencriptar(texto):    
    mitad = len(texto)//2    
    print(texto)
    if(len(texto)%2!=0):        
        texto = texto[mitad+1 : ] + texto[ : mitad+1]
    else:
        texto = texto[mitad : ] + texto[ : mitad]
    print(texto)
    aux = texto[1:len(texto)-1]    
    texto = texto[0]+aux[::-1]+texto[len(texto)-1]    
    print(texto)
    texto = CorrimientoIzquierda(texto,math.ceil(math.log2(len(texto))))        
    print(texto)
    return texto

U=Encriptar("Nayeli")
print(U)
print("\n\n\n")
print(Desencriptar(U))