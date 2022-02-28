#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:28:52 2022

@author: giulianalaspina
"""

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt

import os
abspath = os.path.abspath("prova.py")
dname = os.path.dirname(abspath)
os.chdir(dname)

P=pd.read_csv("Height of Male and Female by Country 2022.csv")

P.info()




#regressore, una variabile x (altezza uomini colonna 2)

x=P.iloc[:,2]
# a noi serve un array e non una serie, quindi:
x=P.iloc[:,2].values.reshape(199,1)   

#la regressa che sarà la mia y (altezza donne colonna 3)
y=P.iloc[:,3].values.reshape(199,1)  

from sklearn.linear_model import LinearRegression
R=LinearRegression()

#creo il modello  M
M=R.fit(x,y)
#abbiamo un'equazione del tipo
"""
y= coef_ * x  + intercept_
"""

print(M.coef_)
print("la relazione trovata è: ")
print("y = ", M.coef_ , " * x + " ,M.intercept_ )

stima =M.predict(x)
print("lo score è {}".format(M.score(x,y)))
#lo score vicino ad uno è buono

#verifica grafica
plt.figure()
plt.plot(x,y, "ob", markersize=6)
plt.plot(x,stima, "or", markersize=6)

P.corr()











P.describe()
P.plot.box()

P[["meanHeightMale"]].plot.box()

P.hist()
plt.figure("primo grafico")
plt.subplot(2,2,1)

plt.title("Man vs Woman")
plt.plot(P["meanHeightMale"],P["meanHeightFemale"],"ob",markersize=4)

pd.plotting.scatter_matrix(P)

P.cov()
P.corr()

from sklearn.linear_model import LinearRegression
R=LinearRegression()

regressore=P.iloc()
#controlliamo la forma della colonna
regressa=P.iloc()


M=R.fit(regressore, regressa)

print(M.coef_)
print(M.intercept_)

z=M.predict(regressore)
plt.figure()
plt.plot(regressore,regressa, "ob", markersize=10)
plt.plot(regressore, z, "or")

z.mean()

