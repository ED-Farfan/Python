def pedirNumeroDeDigito():
    bandera = True
    while(bandera):
        print("\n\n")        
        num=int(input("Ingrese en numero de digitos de su numero: "))
        if(num >= 1):
            bandera = False
        else:
            print("\nIngrese un valor mayor o igual a 1\n")
    return num
def Pregunta(num=0):
    bandera=True
    fin = 0;    
    while(bandera):
        print("¿Este digito (+"str(num)"+)pertenece a su número? (si o no)")
        res=""
        res=input()
        if(res.lower() == "si"):
            ban = True
            while(ban):
                res=input("¿Esta en la posicion correcta?")
                if(res.lower() == "si"):
                    fin = 2
                    ban = False
                elif(res.lower() == "no"):
                    fin = 1
                    ban = False
                else: 
                    print(("\nIngrese lo que se le solicite\n"))
            bandera = False
        elif(res.lower() == "no"):
            bandera = False
        else:
            print(("\nIngrese lo que se le solicite\n"))
    return fin

def Solicitar_Si_Algun_Numero_Es_Correcto(num=[],fin=[]):
    print("\n\n")
    print("Recuerde que el lugar es de la siguiente manera:")
    print("        [0 1 2 3 4 5 6 ...]")
    print(num)
    print("\n")
    u=0
    lista = []
    for i in num:
        res=Pregunta(i)
        if(res == 1):
            lista.append(i)
        elif(res == 2):
            lista.append(i)
            fin[u] = i
        u += 1
    return lista[:],fin[:]

def Juego():
    dig = pedirNumeroDeDigito()
    fin = []
    for i in range(0,dig):
        fin.append(99)
    candidatos = list(range(0,10))
    num = []   
    if(dig > len(candidatos)):
        num,fin = Solicitar_Si_Algun_Numero_Es_Correcto(dig,fin[:])
    else:
        while(99 in fin  and candidatos != []):
            number = len(candidatos) - dig
            lis = []
            if(number >= 1 ):
                for i in candidatos:
                    lis.append(i)
                    candidatos.remove(i)
            else:
                lis = dig[:]
            lis,fin = Solicitar_Si_Algun_Numero_Es_Correcto(dig,fin[:])
            num += lis
    bandera = True
    while(bandera):
        

        
        

    
        

    

