# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:05:52 2022

@author: gugli
"""

import pandas as pd
import numpy as np

DF=pd.read_csv("Height of Male and Female by Country 2022.csv")
DF.info()
DF.head()
DF.tail()
DF.iloc[0,:]
DF2 = pd.DataFrame({"nazione":DF.iloc[:,1],"male_h":DF.iloc[:,2],"female_h":DF.iloc[:,3]})

DF2.describe()

DF2.plot.box()
DF2.hist()
DF2.hist(bins=5)

#normalizzazione 01

denominatore=DF2["male_h"].max()-DF2["male_h"].min()
DF2 ["maschi_normalizzati"] = (DF2["male_h"]-DF2["male_h"].min())/denominatore

denominatore2=DF2["female_h"].max()-DF2["female_h"].min()
DF2 ["femmine_normalizzate"] = (DF2["female_h"]-DF2["female_h"].min())/denominatore2

DF2.plot.box()
DF2.maschi_normalizzati.plot.box()
DF2.femmine_normalizzate.plot.box()

DF2[["maschi_normalizzati","femmine_normalizzate"]].plot.box()

#normalizzazione Z-score ("punteggio Z") DA RIVEDERE 

DF2["maschi_normalizzati"] = (DF2["maschi_normalizzati"]-DF2["maschi_normalizzati"].mean())/DF2["maschi_normalizzati"].std()
DF2["femmine_normalizzate"] = (DF2["femmine_normalizzate"]-DF2["femmine_normalizzate"].mean())/DF2["femmine_normalizzate"].std()

#esercizio sui voti

voti1=np.array([7,6,6,7])
voti2=np.array([9,8,9,6])

m1=voti1.mean()
m2=voti2.mean()

s1=voti1.std()
s2=voti2.std()


z1=(voti1-m1)/s1
z2=(voti2-m2)/s2

rank=z1+z2
DF2["maschi_normalizzati"].plot()
DF2["femmine_normalizzate"].plot()

DF2["male_h"].plot()
DF2["female_h"].plot()

MF=(DF2["maschi_normalizzati"]>=0) & (DF2["femmine_normalizzate"] >=0)
mf=(DF2["maschi_normalizzati"]<0) & (DF2["femmine_normalizzate"]< 0)
Mf=(DF2["maschi_normalizzati"]>=0) & (DF2["femmine_normalizzate"] <0)
mF= (DF2["maschi_normalizzati"]<0) & (DF2["femmine_normalizzate"] >=0)
type (MF)
MF.describe()

print("le nazioni ++ sono {}".format(MF.sum()))
print("le nazioni -- sono {}".format(mf.sum()))
print("le nazioni +- sono {}".format(Mf.sum()))
print("le nazioni -+ sono {}".format(mF.sum()))



DF2["nazione"][mF]
DF2["nazione"][Mf]
DF2[DF2["nazione"]=="Italy"]

# introdurre GroupBy

DF2["MF"]=MF
DF2.maschi_normalizzati.nunique()
DF2.femmine_normalizzate.nunique()

G=DF2.groupby(MF) #crea automaticamente dei sotto gruppi sui quali ragionare
G.male_h.plot.hist()
G.male_h.plot.box()

G.mean()
G.std()
G.median()

from matplotlib import pyplot as plt
plt.plot(DF2["male_h"])

