import os
import math
TAMAÑO_BUFFER = 1500

def obtener_archivos(ruta = '.'):
    contenido = os.listdir(ruta)
    return contenido[:]
def Tamaño_Bytes(ruta = None):
    if(ruta == None):
        return None
    else:
        if(Existe_Archivo(ruta)):            
            archivo = open(ruta, "rb")            
            contenido = archivo.read()            
            archivo.close()
            return len(contenido)
def Existe_Archivo(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
def Convertir_Numero_String(numero = 0,digitos=2):
    dato = str(numero)
    while(len(dato)<digitos):
        dato= '0'+dato
    return dato[:]
def CORTAR_DATO(cadena="",simbolo='&'):
    texto =[]
    aux = ""
    cade=cadena[:]
    if(len(cadena)>5):
        if(cadena[:8]=="NEW-FILE"):            
            cont = 0
            for i in cade:
                if(i!=simbolo):
                    aux += i
                else:
                    cont += 1
                if(cont == 1):
                    texto.append(aux[:])
                    aux = ""
                else:
                    cont = 0
            texto.append(aux[:])
        elif(cadena[:8]=="END-FILE"):
            texto.append(cadena[:])
        else:
            i = 0
            while cadena[i]!=simbolo:
                i+=1
            texto.append(cadena[:i])
            texto.append(cadena[i+2:])
        return texto[:]
def LeerArchivo_Num_Caracteres(ruta=None,inicio=0,caracteres=TAMAÑO_BUFFER):
    if(ruta != None):
        if(Existe_Archivo(ruta)):
            archivo = open(ruta, "rb")
            archivo.seek(inicio)
            contenido = archivo.read(caracteres)
            archivo.close()
            return contenido[:]            
        else:
            return None
    else:
        return None
def Agregar_Datos_Archivo(ruta=None,datos=None):
    if(ruta != None and datos != None):
        if(Existe_Archivo(ruta)):
            archivo = open(ruta, "ab")
            archivo.write(datos)
            archivo.close()
            return 1
        else:
            archivo = open(ruta, "wb")
            archivo.write(datos)
            archivo.close()
            return None
    else:
        return None
def Convertir_Texto_a_Binario(txt):
    return txt.encode('utf-8')
def Convertir_Binario_Texto(txt):
    return txt.encode('utf-8')

def prueba(ruta ):
    txt ="Prueba"
    U=txt.encode('utf-8')
    print(U)
    print(U.decode('utf-8'))
    archivo = open(ruta, "rb")            
    contenido = archivo.read(TAMAÑO_BUFFER)  
    a=contenido.decode('latin-1')          
    archivo.close()
    
    print(type(contenido))
    print(type(a))
    
    print(len(a))
    print(a.encode('latin-1')==contenido)
    aux ="nuevo archivo &&&&"
    print(aux.encode('latin-1'))
    asa = aux.encode('latin-1')+contenido
    print("\n\n\n\n")
    print(len(asa.decode('latin-1')))    

def Prueba2(ruta):
    
    
    contenido = LeerArchivo_Num_Caracteres(ruta,123)
    a=contenido.decode('latin-1')              
    
    print(type(contenido))
    print(type(a))  
    print(len(a))
    iteraciones = math.ceil(Tamaño_Bytes("UNAM.pdf")/TAMAÑO_BUFFER)
    inicio = 0
    print("Numero de paquetes: "+str(iteraciones))
    for i in range(iteraciones):
        contenido = LeerArchivo_Num_Caracteres(ruta,inicio)
        a=contenido.decode('latin-1')
        inicio += len(a)
        Agregar_Datos_Archivo("Copia.pdf",contenido)
        print("Datos leidos["+str(len(a))+"] numero de paquete: "+str(i))


#print(obtener_archivos())
#print(math.ceil(Tamaño_Bytes("UNAM.pdf")/TAMAÑO_BUFFER))
#prueba("UNAM.pdf")
#print(Convertir_Numero_String(2344,12))
print(CORTAR_DATO("NEW-FILE&&UNAM.pdf&&3&&512"))
print(CORTAR_DATO("END-FILE"))
print(CORTAR_DATO("094&&asaasjasijhasfhjasfnhjksdgfjhsdkdf"))
Prueba2("UNAM.pdf")