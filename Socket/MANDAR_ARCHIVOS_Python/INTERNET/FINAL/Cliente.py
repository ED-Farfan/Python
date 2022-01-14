import os
import math
from socket import *
TAMAÑO_BUFFER = 1500
PUERTO=1998

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
    return txt.encode('latin-1')
def Convertir_Binario_Texto(txt):
    return txt.decode('latin-1')

def Crear_Archivo(sock,nombre):
    name = nombre
    i = 0
    t = 0
    while 1:
        m = sock.recvfrom(TAMAÑO_BUFFER)
        r = CORTAR_DATO(Convertir_Binario_Texto(m[0]))
        tam = len(m[0])
        print("\n Recibo paquete["+str(i)+"] bytes: "+str(tam)+"\n")        
        if(r[0]=="END-FILE"):
            print("Termine de almacenar "+name+" Total: "+str(t)+" Bytes \n ")
            break
        else:
            if(int(r[0])==i):
                t += tam
                datos = Convertir_Texto_a_Binario(r[1])
                Agregar_Datos_Archivo(name,datos)
                i += 1
            else:
                print("\nNo se completo la descarga de "+name+"\n")
                os.remove(name)
                break

    Agregar_Datos_Archivo(ruta=None,datos=None)
def Decidir():
    s=socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('',PUERTO))
    print("Espero")
    while 1: 
        m=s.recvfrom(TAMAÑO_BUFFER)
        r = CORTAR_DATO(Convertir_Binario_Texto(m[0]))
        if(r[0]=="NEW-FILE"):
            if(Existe_Archivo(r[1])!= True):
                print("Archivo: "+r[1])
                Crear_Archivo(s,r[1])
                #break
            else: 
                print("Ya existe el Archivo: "+r[1])

    
Decidir()