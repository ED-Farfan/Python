import os
import math
import struct
import sys
import time
from socket import *
TAMAÑO_BUFFER = 1500
Esperar = .2
PUERTO = 1998
def Existe_Carpeta(ruta):    
    if os.path.isdir(ruta):
        return 1
    else:
        return 0
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
def Crear_Carpeta(ruta):
    if(Existe_Carpeta(ruta)==0):
        os.mkdir(ruta)
        return 1
    else:
        return 2
def Convertir_Texto_a_Binario(txt):
    return txt.encode('latin-1')
def Convertir_Binario_Texto(txt):
    return txt.decode('latin-1')

def Mandar_Archivo(nombre,sock):
    if(Existe_Archivo("Mandar/"+nombre)):
        ruta = "Mandar/"+nombre
        tam = Tamaño_Bytes(ruta)                        
        Digitos = len(str(tam))
        paquetes=math.ceil(tam/(TAMAÑO_BUFFER-Digitos-2))
        text="NEW-FILE&&"+nombre+"&&"+str(Digitos)+'&&'+str(paquetes)
        print("Mando: "+text)        
        sock.sendto(Convertir_Texto_a_Binario(text), (host,PUERTO))
        time.sleep(Esperar*3)
        inicio = 0
        for j in range(0,paquetes):
            contenido = LeerArchivo_Num_Caracteres(ruta,inicio,TAMAÑO_BUFFER-Digitos-2)
            mensaje = Convertir_Numero_String(j,Digitos)
            a= Convertir_Binario_Texto(contenido)
            mensaje+="&&" + a
            print("\nMando: Paquete["+str(j)+":"+str(paquetes-1)+"]" +"Bytes: "+str(len(a))+" \n\tNombre Archivo: "+nombre+"\n\t   ->Tamaño total: "+str(tam)+" bytes")
            sock.sendto(Convertir_Texto_a_Binario(mensaje), (host,PUERTO))                            
            inicio += len(Convertir_Binario_Texto(contenido))
            time.sleep(Esperar)
        sock.sendto(Convertir_Texto_a_Binario("END-FILE"), (host,PUERTO))
        print("\n\n")
    else:
        return False
def Mandar_Archivos(sock):
    if(Crear_Carpeta("Mandar")==2):
        Prioridad = obtener_archivos("Mandar")
        Mandados =[]
        while 1:
            if(len(Mandados)==0):
                for i in Prioridad:
                    print("\nMandando archivo con prioridad: "+i+"\n")
                    time.sleep(Esperar)
                    Mandar_Archivo(i,sock)
                    Mandados.append(i)
                    Prioridad.remove(i)
            else:
                Prioridad = obtener_archivos("Mandar")                    
                for i in Prioridad:
                    if(i in Mandados):
                        Prioridad.remove(i)                    
                for i in Prioridad:
                    print("\nMandando archivo con prioridad: "+i+"\n")
                    time.sleep(Esperar)
                    Mandar_Archivo(i,sock)
                    Mandados.append(i)
                    Prioridad.remove(i)
                for i in Mandados:
                    print("\nRenvio archivo: "+i+"\n")
                    time.sleep(Esperar)
                    Mandar_Archivo(i,sock)                                        

s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

#host = 'localhost'
host='192.168.1.255'
Mandar_Archivos(s)