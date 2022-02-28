# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:02:10 2022

@author: gugli
"""

import numpy as np
from matplotlib import pyplot as plt

#costruiamo una funzione y della variabile x

x= np.linspace(0,10,100) #min max e numero di tagli

y=np.cos(x) #coseno
z=np.sin(x) #seno


#realizziamo un plot sul piano cartesiano 
plt.figure("la mia figura")
plt.title("un esempio di funzioni armoniche", fontsize=24,color="red")
plt.plot(x,y, color="magenta", linewidth=5, linestyle="dotted") #color=(1,0,0)
plt.plot(x,z, color="blue", linewidth=5, linestyle="dotted")
plt.xlabel("Variabile indipendente", fontsize=12,color="blue")
plt.ylabel("variabile dipendente", fontsize=12,color="purple")
plt.grid(True)
plt.xlim([-2,12])
plt.ylim([-2,2])
plt.xticks(np.arange(-2,12,1))#arange prende min max e intervallino in cui dividere
plt.yticks(np.arange(-2,2,1))
plt.legend(["cos(x)","sin(x)"],fontsize=12)

plt.text(1.5,1.1, "MAX", fontsize=30, color="green")
plt.show() #chiude la figura

plt.figure("Stile matlab")
plt.plot(x,y,"Dk",linewidth=4) #:m sta per magenta , "ok" dotted black, variazione stile mathlab


