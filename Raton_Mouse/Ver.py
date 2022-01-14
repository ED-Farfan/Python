import keyboard
import pyautogui as pa
import time
import random
from datetime import date
from datetime import datetime
from os import system


ancho,alto = pa.size()
print(pa.position())
T_inicial = datetime.now()
time.sleep(10)
TOTAL = 0
for i in range(36000):    
    TOTAL += 1
    system("clear")
    pa.moveTo(x=random.randint(1,ancho),y=random.randint(1,alto))
    print(pa.position())
    print("Tiempo de trabajo aproximado: ",datetime.now()-T_inicial)
    print("Click totales: "+str(TOTAL))
    time.sleep(1)
    #pa.typewrite("Hola que haces \n") #EScribir
Hola = False

#while True:
 #   if(keyboard.is_pressed('98')):
  #      print("Termino")
   #     break
    
   # elif(keyboard.is_pressed('hola')):
   #     Hola = not(Hola)
    #    print("Palabra secreta")
   # elif(Hola):
    #    print(pa.position())
    #else:
     #   time.sleep(.5)