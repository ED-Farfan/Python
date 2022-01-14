def encriptar(texto):
    if(len(texto)==2):
        return texto[::-1]
    elif(len(texto)==1):
        return texto
    elif(len(texto)==0):
        return ""
    elif(len(texto)%2==0):#Cadena par
        L=[]
        u=""
        for i in range(len(texto)):
            if(i%2!=0):  
                    u+=texto[i]
                    L.append(u[:])
                    u=""
            else:
                u+=texto[i]
        for i in range(len(L)):
            L[i] = encriptar(L[i])
        aux = "".join(L)
        texto_aux = aux[1:len(aux)-1]
        texto_aux = encriptar(texto_aux)        
        return aux[0]+texto_aux+aux[len(aux)-1]
    elif(len(texto)%2!=0):
        aux = texto[:len(texto)-1]
        aux = encriptar(aux)
        return aux + texto[len(texto)-1]
def desencriptar(texto):
    if(len(texto)==2):
        return texto[::-1]
    elif(len(texto)==1):
        return texto
    elif(len(texto)==0):
        return ""
    elif(len(texto)%2==0):#Cadena par
        texto_aux = texto[1:len(texto)-1]
        texto_aux = desencriptar(texto_aux)
        texto_aux = texto[0]+texto_aux+texto[len(texto)-1]
        L=[]
        u=""
        for i in range(len(texto_aux)):
            if(i%2!=0):  
                    u+=texto_aux[i]
                    L.append(u[:])
                    u=""
            else:
                u+=texto_aux[i]
        for i in range(len(L)):
            L[i] = desencriptar(L[i])
        return "".join(L)
    elif(len(texto)%2!=0):
        aux = texto[:len(texto)-1]
        aux = desencriptar(aux)
        return aux + texto[len(texto)-1]
U="CURSO DE CRIPTOGRAFÍA"

encrip = encriptar(U)
print(encrip)
texto = desencriptar(encrip)
print(texto)

