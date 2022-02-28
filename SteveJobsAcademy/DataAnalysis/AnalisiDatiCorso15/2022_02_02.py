# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:02:58 2022

@author: gugli
"""

import pandas as pd
import numpy as np

import os #per parlare con il sistema operativo

abspath = os.path.abspath("2022_02_02.py") #percorso assoluto
dname = os.path.dirname(abspath) #directory di questo script
os.chdir(dname) #ora la directory è la stessa

# https://archive-beta.ics.uci.edu/ 
#www.kaggle.com/datasets
#.csv comma separated value ; .data;

#importiamo i dati in una tabella

#DF= pd.read_csv("wine.data") #per funzione csv tratta il primo rigo come nomi
names = ["tipo","Alcohol","Malic acid","Ash","Alcalinity of Ash","Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280_OD315 of diluted wines","Proline"]

DF= pd.read_csv("wine.data") 
DF.columns = names


DF.info()
DF.shape
DF.describe()

Colonna = DF ["tipo"]
Colonna2=DF.tipo

DF2 = pd.DataFrame({"T":DF.tipo,"Alc": DF.Alcohol, "Ceneri":DF.Ash})
DF2.shape
DF2.info()
DF2.describe()
DF2.median()
DF2.max()
DF2.min()

#quanti valori differenti contiene una colonna?

DF2["T"].nunique()

#quali sono i numeri ripetuti in colonna?

DF2["T"].unique()

#stampa quante volte c'è ciascun valore

for valore in DF2["T"].unique():
    print ( " il tipo {} compare {} volte".format(valore,(DF2["T"]==valore).sum()))
    
    
#esempio creazione DataFrame
    
N=["Alice","Beatrice","Carla"]
H=[120,115,118]
AGE=[5,6,5]

bimbe=pd.DataFrame({"alt":H,"anni":AGE})
bimbe2=pd.DataFrame({"alt":H,"anni":AGE},index=N)


#posso recuperare gli elementi della tabella (DataFrame) in vari modi
#Prima colonna, primo elemento

bimbe2.iloc[0,0]
bimbe2.loc["Alice","alt"]
bimbe2.loc["Alice"][0]
bimbe2.loc["Alice"]["alt"]
bimbe2["alt"]["Alice"]

#altro esempio ambiguo 
C=[0,2,1]
K=pd.DataFrame({"colonna":AGE},index=C)
K.iloc [0]
K.iloc[2]
K.loc[2]
#loc usa gli indici personalizzati
#iloc usa gli indici automatici


DF2 
# il valore medio dell'alcool per i vini di tipo 1 è diverso dal valore
#medio per quelli di tipo 2?

#estrazione booleana per scegliere le righe

T1=DF2["Alc"][DF2["T"]==1]
T2=DF2["Alc"][DF2["T"]==2]
T3=DF2["Alc"][DF2["T"]==3]

print("Media del tipo {} vale {:.3f}".format(1,T1.mean()))
print("Media del tipo {} vale {:.3f}".format(1,T2.mean()))
print("Media del tipo {} vale {:.3f}".format(1,T3.mean()))

#c'è un modo più facile

#crea soltanto e colloca in memoria
DF2.groupby("T")

#corretto: (calcolo media per gruppo)
DF2.groupby("T").mean()

DF2.groupby("T").max()

DF2.groupby("T").min()

DF2.groupby("T").std()

DF2["T"].hist()

DF2["Alc"].hist()

DF2["Alc"].hist(bins=4)



#regola di Sturgis 
#una buona scelta di bins è 1+log_2(N) #np.log2(178) viene 7.47

DF2["Alc"].hist(bins=8)
DF2.hist(bins=8)


#altezza delle colonnine con esattezza? esercizio (count??)