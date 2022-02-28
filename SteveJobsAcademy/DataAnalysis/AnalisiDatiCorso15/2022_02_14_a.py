# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:35:19 2022

@author: gugli
"""

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt

import os
abspath = os.path.abspath("2022_02_14.py")
dname = os.path.dirname(abspath)
os.chdir(dname)


#1 importare i dati dal file csv in un datadrame

pottery=pd.read_csv("pottery.csv")

#2info generali
pottery.info()

#3 info statistiche std=dev standard, mean = media 

pottery.describe()

pottery.plot.box() # 4 range tutte le colonne numeriche

#prendere solo alcune colonne
pottery[["Fe","Mg","Ca","Na"]].plot.box()
# I dati sono bilanciati/simmetrici verso la media? In questo caso no, la linea verde
#che indica la media sia su Fe che Mg sono oltre e di molto il punto medio.
#Ca e Na si vedono troppo piccoli, quindi
pottery["Na"].plot.box()
#Puntini in alto? Valori fuori scala

pottery.hist() #picco modale, ci fa vedere gruppi
#distinti e sottogruppi

pottery[["Fe","Mg","Ca","Na"]].hist()


plt.figure("primo grafico")
plt.subplot(2,2,1) #2 r 2 col, disegniamo sul n 1
#subplot 1|2
#        3|4

plt.title("Al vs Fe")
plt.plot(pottery["Al"],pottery["Fe"],"ob",markersize=4) 
#ob = pallino blu

plt.subplot(2,2,2) 
plt.title("Fe vs Mg")
plt.plot(pottery["Fe"],pottery["Mg"],"ob",markersize=4) 

plt.subplot(2,2,3) 
plt.title("Mg vs Na")
plt.plot(pottery["Mg"],pottery["Na"],"ob",markersize=4) 

plt.subplot(2,2,4) 
plt.title("Fe vs Na")
plt.plot(pottery["Fe"],pottery["Na"],"ob",markersize=4) 
#su console %matplotlib QT serve a far vedere in grande (no W11)

#Voglio un plot di Al vs Fe dove ogni osservarzione 
#il colore dipende dal sito da cui proviene"

#quanti siti?

pottery["Site"] #pottery.Site è uguale

pottery.Site.value_counts() #conta valori
pottery.Site.nunique() #valori unici (4)
pottery.Site.unique() # restituisce valori unici

#raggruppiamo per siti
G=pottery.groupby("Site")
figure("seconda figura")
plt.title("Al vs Fe per site")
#creiamo 4 dataframe per o 4 siti di scavo
#plt.plot(pottery["Al"] [pottery["Site"]== 'Llanedyrn'])
p1=pottery[pottery["Site"]=='Llanedyrn']
p2=pottery[pottery["Site"]=='Caldicot']
p3=pottery[pottery["Site"]=='IsleThorns']
p4=p2=pottery[pottery["Site"]=='AshleyRails']

plt.plot(p1["Al"],p1["Fe"],"ob", markersize=8)
plt.plot(p2["Al"],p2["Fe"],"or",markersize=8)
plt.plot(p3["Al"],p3["Fe"],"og",markersize=8)
plt.plot(p4["Al"],p4["Fe"],"om",markersize=8)

#Varianza = {x1....xn} , calcolo media !!! IMPORTANTE
# 1/n * Somma [(xi-m)(xi-m)]

#Covarianza 1/n * Somma [(xi-m) (yi-m)]

#Al = [10,12,10,14] mediaAl = 11,5
#Fe = [8,4,4,6] mediaFe = 5,5

#varianza Al = (10-11.5)^2 + (12-11,5)^2 + (10-11,5)^2+ (14+9,5^2)
#               __________________________________________________
#                                       4
#Ci sono 2 scuole di pensiero. "Statistici" e "matematici"
#Statistici = 1/n Somm(...)=var (numphy)
#Matematici = 1/n-1 Somm (...)=var (Foglio elett)
#Su tante osservazioni cambia nulla

al=np.array([10,12,10,14])
al.var() 

fe=np.array([8,4,4,6])
fe.var()

np.cov(al,fe)

# VAR, COV
# COV, VAR

#Segno dei COV? Ci dice se quando aumenta l'uno l'altro aumenta e 
#se quando diminuisce uno l'altro diminuisce

#studiamo la correlazione tra colonne 
pd.plotting.scatter_matrix(pottery)
#solo alcune colonne
pd.plotting.scatter_matrix(pottery[["Al","Mg","Fe"]])


#covarianza
pottery.cov()
#correlazione
pottery.corr()

#Regola pratica:
    #se la correlazione è tra -1 e -0.7 è una forte correlazione negativa
    #se la correlazione è tra -0.7 e -0.3 è una debole correlazione negativa
    #se è tra -0.3 e +0.3 non c'è una buona correlazione
    #se è tra +0.3 e 0.7 è una debole correlazione positiva
    #se è tra 0.7 3 +1 forte correlazione positiva
    
P=pd.read_csv("pirates-vs-global-warming.csv")    

P.info()

P.corr()




























