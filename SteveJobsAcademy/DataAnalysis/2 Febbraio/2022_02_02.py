# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 08:58:57 2022

@author: Giovanni
"""


import pandas as pd
import numpy as np


import os # per parlare CON IL SISTEMA OPERATIVO
# 3 righe per posizionarci automaticamente 
# nella stessa directory del file che tiamo
# editando
abspath = os.path.abspath("2022_02_02.py") # percorso assoluto di questo script
dname = os.path.dirname(abspath) # directoy di questo script
os.chdir(dname) # la directory di lavoro è adesso la stessa dello script
####

#importiamo i dati
#DF=pd.read_csv("wine.data", header=None) #header none mette nelle prime colonne i numeri ordinati


#creare lista nomi per dare dei nomi alle colonne
nomi=["Tipo","Alcohol", "Malic acid","Ash", "Alcalinity of ash","Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols","Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines","Proline"]
DF=pd.read_csv("wine.data", header=None)
DF.columns=nomi
DF.info()
DF.shape #ci dice quante righe e quante colonne ci sono

DF.describe()

#un dataframe è un dizionario dove le chiavi sono i nomi delle colonne
#e i valori sono le colonne stesse

#estraiamo una colonna dal dataframe

Colonna = DF["Tipo"] #sto estraendo la colonna Tipo

Colonna2 = DF.Tipo #secondo modo per estrarre una colonna

Colonna3 = DF.iloc[:,0] #estrarre con gli indici numerici

#creare il nostro dataframe
DF2 = pd.DataFrame({"T":DF.Tipo, "A":DF.Alcohol, "C":DF.Ash})

DF2.info()

DF2.describe()

#alcune funzioni 

DF2.mean()
DF2.var()
DF2.std()


#informazioni delle singole colonne
#quanti valori diversi contiene la colonna?

DF2["T"].nunique()

#quali sono i numeri ripetuti in colonna?

DF2["T"].unique()

#quando vale 1?

DF2["T"]==1 #valori booleani dove vero è quando restituisce uno

#posso sommare i booleani veri che sono uguali ad uno per capire quanti valori che mi interessano ci sono
(DF2["T"]==1).sum()


#facciamo stampare quante volte c'è un valore

for valore in DF2["T"].unique():
    print ("il tipo di valore {} compare {} volte ".format(valore, (DF2["T"]==valore).sum()))



#esempio

N=["Giuliana", "Ilaria", "Alessandra"]
H=[165, 168, 161]
Age= [29, 27, 30]

bimbe=pd.DataFrame({"altezza":H, "anni":Age})
bimbe2=pd.DataFrame({"altezza":H, "anni":Age}, index=N)


#prima colonna di ogni elemento
bimbe2.iloc()[0][0]
bimbe2.iloc()[0,0]
bimbe2.loc["Alessandra", "altezza"]
bimbe2.loc["Ilaria"] [0]

# esempio

C=[0,2,1]
K=pd.DataFrame({"colonna":Age}, index=C)
K.iloc[0]
K.iloc[2]
K.loc[2]
#loc usa gli indici automatici, iloc usa gli indici personalizzati

#il valore medio dell'alcol per i vini di tipo 1
#è diverso dal valore medio dell'alcol per i vini di tipo 2?

#creo un oggetto da DF2

#estrazione booleana
#uno una colonna di booleani per scegliere le righe

A1=DF2["A"][DF2["T"]==1] #prendo solo gli elementi vero della colonna
A2=DF2["A"][DF2["T"]==2]
A3=DF2["A"][DF2["T"]==3]

print("media del tipo {} vale {:.3f}".format(1, A1.mean()))
print("media del tipo {} vale {:.3f}".format(2, A2.mean()))
print("media del tipo {} vale {:.3f}".format(3, A3.mean()))

#esiste un modo più semplice di estrazione con groupby

DF2.groupby("T") #crea l'oggetto ma non lo usa
DF2.groupby("T").mean() #ragruppa in base ai valori che trova nella t

#groupby calcola anche i sottogruppi

DF2.groupby("T").max()

DF2.groupby("T").std()


DF2["A"].nunique()

DF2.groupby("A").mean()


#possiamo ridurre il numero dei gruppi con np.round

DF2["A-approx"]=np.round(DF2["A"],0) #aggiunge colonna approssimata

DF2["A-approx"].nunique()
DF2.groupby("A-approx").mean()



#instogramma
DF2["T"].hist() #stampa in console l'instogramma dei dati
DF2["A"].hist()

DF2["A"].hist(bins=2)
 #l'instogramma dipende dal numero di bin che voglio considerare 
 #più oggetti più bin e viceversa
 
 
 #regola di Sturgis, una buona scelta è 1+Log_2(N)
 
 
#np.log2(178)
#7.475733430966398

DF2["A"].hist(bins=8) #istogramma più esplicativo dopo la regola dei bins

#se lo faccio su tutto il dataframe
DF2.hist(bins=8)


#esercizio
#trovare il numero delle colonne preciso con il count



























