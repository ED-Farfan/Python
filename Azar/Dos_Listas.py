import random 
#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime


def Asignar(Nombres,Tareas):        
    Asignado = []
    for i in Nombres:
        Asignado.append([i[:]])
    Puesto = []
    while(len(Tareas)!= 0):
        if(len(Puesto)==0):
            Puesto = list(range(len(Nombres)))
        else:
            random.shuffle(Tareas)
            random.shuffle(Puesto)
            Asignado[Puesto.pop()].append(Tareas.pop())
    return Asignado[:]
def Mostrar(Asignado):
    print("\n\n\n\n\n")
    print("Resutados:")
    print("\n")
    for i in  Asignado:
        print("*"+i[0])
        l = i[1:]
        for y in l:
            print("\t->"+y)
        print("\n")
    print("\n")
    
    #Día actual
    today = date.today()
    #Fecha actual
    now = datetime.now()
    print("Fecha de resultados: ",now)
    print("\n")
    print("\n")
Nombres =[]	
Nombres.append("Erick David Farfan Sanchez")
Nombres.append("Alfredo De Jesus Amaya Camargo")
Nombres.append("Valle Erick Benavides Del")
Nombres.append("Pedro Manuel Quiroz Palacios")
Nombres.append("Carlos Alberto Vasquez Blanco")
Tareas = ["Pares trenzados","Cable coaxial","fibra óptica","Radio enlaces VHF y UHF","Microondas","Infrarrojos (como fibra óptica pero por el aire)","Satélite","Ondas de radio"]
Mostrar(Asignar(Nombres,Tareas))