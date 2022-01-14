import os
import math
import socket
import struct
import sys
import time
TAMAÑO_BUFFER = 1500
#multicast_addr = '224.0.0.1'
multicast_addr = "192.168.1.255"
port = 3000
Trabajar = 1
Esperar = 0.5
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
def Crear_Sock():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ttl = struct.pack('b', 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)        
    except :
        return -2,None
    finally:
        return 1 , sock
def Mandar_Archivos_RED(sock,ruta,nombre):
    tam = Tamaño_Bytes(ruta)                        
    Digitos = len(str(tam))
    paquetes=math.ceil(tam/(TAMAÑO_BUFFER-Digitos-2))
    text="NEW-FILE&&"+nombre+"&&"+str(Digitos)+'&&'+str(paquetes)
    print("Mando: "+text)
    sock.sendto(Convertir_Texto_a_Binario(text), (multicast_addr, port))
    time.sleep(Esperar*3)
    inicio = 0
    for j in range(0,paquetes):
        contenido = LeerArchivo_Num_Caracteres(ruta,inicio,TAMAÑO_BUFFER-Digitos-2)
        mensaje = Convertir_Numero_String(j,Digitos)
        a= Convertir_Binario_Texto(contenido)
        mensaje+="&&" + a
        print("\nMando: Paquete["+str(j)+":"+str(paquetes-1)+"]" +"Bytes: "+str(len(a))+" \n\tNombre Archivo: "+nombre+"\n\t   ->Tamaño total: "+str(tam)+" bytes")
        sock.sendto(Convertir_Texto_a_Binario(mensaje), (multicast_addr, port))                            
        inicio += len(Convertir_Binario_Texto(contenido))
        time.sleep(Esperar)
    sock.sendto(Convertir_Texto_a_Binario("END-FILE"), (multicast_addr, port))
    print("\n\n")
def Mandar_Archivos():
    if(Crear_Carpeta("Mandar")==2):
        Prioridad = obtener_archivos("Mandar")
        num,sock= Crear_Sock()
        if(num != 1):
            return -10
        if(len(Prioridad )> 0):
            Mandados = []            
            while Trabajar == 1:
                if( len(Mandados)==0):
                    print("Archivos: ")
                    print(Prioridad)
                    for i in Prioridad:
                        
                        Mandar_Archivos_RED(sock, "Mandar/"+i,i)                                                
                        Mandados.append(i)
                        Prioridad.remove(i)
                else:
                    time.sleep(Esperar*5)
                    Prioridad = obtener_archivos("Mandar")                    
                    for i in Prioridad:
                        if(i in Mandados):
                            Prioridad.remove(i)                    
                    if(len(Prioridad)!=0):
                        for i in Prioridad:                          
                            Mandar_Archivos_RED(sock, "Mandar/"+i,i)
                            Mandados.append(i)
                            Prioridad.remove(i)
                    print("\n\nArchivos: ")
                    print(Mandados)
                    for i in Mandados:                     
                        Mandar_Archivos_RED(sock, "Mandar/"+i,i)
                        

        else:
            return -3    
    else:
        return 2
print(Mandar_Archivos())