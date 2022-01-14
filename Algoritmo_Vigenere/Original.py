import string 
def Cifrar(dic,Codificar,clave):
    R = ""
    L = list(dic.keys())
    N = list(dic.values())
    for i in range(0,len(Codificar)):
        if(Codificar[i] in L):
            res = (dic[Codificar[i]]+dic[clave[i%len(clave)]])%len(dic)
            R += L[res]
        else:
            R += Codificar[i]
    return R
def Descifrar(dic,Decodificar,clave):
    R = ""
    L = list(dic.keys())
    N = list(dic.values())
    for i in range(0,len(Decodificar)):
        if(Decodificar[i] in L):
            res = (dic[Decodificar[i]]-dic[clave[i%len(clave)]])%len(dic)
            R += L[res]
        else:
            R += Decodificar[i]
    return R

min = list(string.ascii_lowercase)
Mayus = list(string.ascii_uppercase)
print(Mayus+min)
dic = dict(zip(Mayus,list(range(0,len(Mayus)))))
Codificar = input("\nIngrese el texto a codificar:\n\t-> ")
Clave = input("\nIngrese la clave:\n\t->")
print("\nMensaje a encriptar: "+Codificar+" Tamaño:"+str(len(Codificar)))
print("\nClave: "+Clave+" Tamaño:"+str(len(Clave))+"\n\n")

Cifrado = Cifrar(dic,Codificar,Clave)
print("\nCifrado: "+Cifrado+"\n")
print(Descifrar(dic,Cifrado,Clave))

