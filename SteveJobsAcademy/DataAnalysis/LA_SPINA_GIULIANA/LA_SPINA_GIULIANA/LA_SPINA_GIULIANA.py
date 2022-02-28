# -*- coding: utf-8 -*-
"""
prova finale del modulo Analisi datiITS Steve JOBS Corso 15
"""

"""
COGNOME STUDENTE: La Spina
NOME STUDENTE: Giuliana

Salva questo file come COGNOME_NOME.py, e consegnalo a fine compito al docente
(esempio ROSSI_FABIO.py)
"""

"""
FOGLIO ELETTRONICO

task 0
Importare il file studenti.csv fornito dal docente in un foglio Google e
denominare tale foglio con il proprio COGNOME_NOME (esempio: ROSSI_FABIO)
Il file al termine della elaborazione andrà salvato in locale sul
tuo computer di lavoro  e consegnato al docente, NON VA CONDIVISO. 

Il significato dei valori riportati nel file è come segue:

AGE:    1, sotto i venti anni
        2: tra i venti e i venticinque
        3: sopra i venticinque
Gender: 1: maschio
        2: femmina
HS_Type:    1: liceo
            2: istituto tecnico
            3: altro
Work:   1: inoccupato
        2: occupato
Partner: 1: single
         2: con partner
Mother edu: interi con grado di istruzione della madre
Father edu: interi con grado di istruzione del padre
#_Siblings: numero di fratelli/sorelle
Study_hrs: ore di studio media quotidiana
Grade: media di profitto

task 1

Calcolare minimo, massimo, media e mediana della colonna Grade
per i gruppi che seguono:
    a) i maschi con padre con istruzione minima
    b) i maschi con padre con istruzione massima
    c) tutti i maschi
    d) tutte le femmine

task 2
Calcolare la percentuale di maschi single e maschi con partner su tutti i maschi
Calcolare la percentuale di femmine single e femmine con partner su tutte le femmine

task 3
Produrre un istogramma della distribuzione dei valori nella colonna Grade

NOTA BENE:
    Tutte le risposte richieste devono essere leggibili e calcolate nel 
    foglio elettronico che consegnerai
"""

"""
PYTHON

task 0
Importare il file studenti.csv fornito dal docente in un DataFrame di Pandas

task 1
Ottenere un diagramma a torta che mostri la provenienza degli studenti da vari
tipi di scuola.

task 2
In unico riquadro ottenere affiancati i box plot relativi ai Grades ottenuti
dai maschi e dei Grades ottenuti dalle femmine

task 3
Quante sono le studentesse con partner che hanno avuto Grade superiore al Grade medio?
Quante sono le studentesse senza partner che hanno avuto Grade superiore al Grade medio?
Quante sono in percentuale sul totale delle femmine le studentesse che hanno Grade superiore al Garde medio?
Quanti sono in percentuale gli studenti maschi sul totale dei maschi che hanno Grade superirore al Grade medio?

task 3
Produrre una scatter matrix dell'intero data set

task 4
Calcolare la correlazione tra tutte le colonne del data set
Trovare la coppia di colonne che mostra il massimo grado di correlazione positiva
Riferiamoci ad esse come colonne A e B
Trovare la coppia di colonne che mostra il massimo grado di correlazione negativa
Riferiamoci ad esse come colonne C e D

task 5
Produrre in una unica figura (ma in tre subplot separati) il plot che mostri
a) la distribuzione dei valori nelle colonne A e B
b) la distribuzione dei valori nelle colonne C e D
c) la distribuzione dei valori nelle colonne A e B colorando di blu i dati relativi ai maschi 
    e rossi quelli relativi alle femmine
    
'
task 6
Calcolare la relazione di regressione lineare che "preveda" B a partire da A
Produrre plot che illustrino tale relazione

"""

"""
task 0
Importare il file studenti.csv fornito dal docente in un DataFrame di Pandas
"""

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt

import os
abspath = os.path.abspath("LA_SPINA_GIULIANA.py")
dname = os.path.dirname(abspath)
os.chdir(dname)


#1 importare i dati dal file csv in un datadrame

S=pd.read_csv("studenti.csv")
S.info()
S.describe()


"""
task 1
Ottenere un diagramma a torta che mostri la provenienza degli studenti da vari
tipi di scuola.

"""

S["HS_TYPE"].value_counts().plot.pie()


"""
task 2
In unico riquadro ottenere affiancati i box plot relativi ai Grades ottenuti
dai maschi e dei Grades ottenuti dalle femmine
"""


plt.figure()
plt.subplot(1, 2,1)
plt.boxplot(S["GRADE"][S["GENDER"]==1])

plt.xlabel("GRADE maschi")
plt.ylim(0, 8)
plt.subplot(1, 2,2)

plt.boxplot(S["GRADE"][S["GENDER"]==2])
plt.xlabel("GRADE femmine")
plt.ylim(0, 8)


"""
task 3
Quante sono le studentesse con partner che hanno avuto Grade superiore al Grade medio?
Quante sono le studentesse senza partner che hanno avuto Grade superiore al Grade medio?
Quante sono in percentuale sul totale delle femmine le studentesse che hanno Grade superiore al Garde medio?
Quanti sono in percentuale gli studenti maschi sul totale dei maschi che hanno Grade superirore al Grade medio?
"""
gradoMedio=S["GRADE"].mean()
studentesse1=S["GENDER"][(S["PARTNER"]==2)&(S["GRADE"]>gradoMedio)]
print("e studentesse con partner che hanno avuto Grade superiore al Grade medio sono: ",len(studentesse1))  



studentesse2=S["GENDER"][(S["PARTNER"]==1)&(S["GRADE"]>gradoMedio)]
print("e studentesse senza partner che hanno avuto Grade superiore al Grade medio sono: ",len(studentesse2))    


totStudentesse=len(S[S["GENDER"]==2])
percentualeT=len(S["GENDER"][(S["GRADE"]>=gradoMedio)])     
print   ((percentualeT*totStudentesse)/100 )
print("% studentesse:", 100*percentualeT/totStudentesse)

totStudenti=len(S[S["GENDER"]==1])
percentualeT=len(S["GENDER"][(S["GRADE"]>=gradoMedio)]) 
print("% studenti:", 100*percentualeT/totStudenti)
                         
"""
task 3
Produrre una scatter matrix dell'intero data set
"""

pd.plotting.scatter_matrix(S)

"""
task 4
Calcolare la correlazione tra tutte le colonne del data set
Trovare la coppia di colonne che mostra il massimo grado di correlazione positiva
Riferiamoci ad esse come colonne A e B
Trovare la coppia di colonne che mostra il massimo grado di correlazione negativa
Riferiamoci ad esse come colonne C e D
"""

correlazione= S.corr()

A=S["MOTHER_EDU"].corr(S["FATHER_EDU"])

S["AGE"].corr(S["STUDY_HRS"])


"""
task 5
Produrre in una unica figura (ma in tre subplot separati) il plot che mostri
a) la distribuzione dei valori nelle colonne A e B
b) la distribuzione dei valori nelle colonne C e D
c) la distribuzione dei valori nelle colonne A e B colorando di blu i dati relativi ai maschi 
    e rossi quelli relativi alle femmine

"""

plt.figure()
plt.subplot(1, 3,1)
plt.plot(S["MOTHER_EDU"],S["FATHER_EDU"], "ob")

plt.subplot(1, 3,2)
plt.plot(S["AGE"],S["STUDY_HRS"], "ob")

plt.subplot(1, 3,3)



plt.plot(S["MOTHER_EDU"][S["GENDER"]==1],\
         S["FATHER_EDU"][S["GENDER"]==1],"ob",markersize=3)
plt.plot(S["MOTHER_EDU"][S["GENDER"]==2],\
             S["FATHER_EDU"][S["GENDER"]==2],"or",markersize=3)
"""
task 6
Calcolare la relazione di regressione lineare che "preveda" B a partire da A
Produrre plot che illustrino tale relazione

"""

from sklearn.linear_model import LinearRegression
R=LinearRegression()


regressore=S["MOTHER_EDU"].values.reshape(145,1)
regressa=S["FATHER_EDU"].values.reshape(145,1)
M=R.fit(regressore, regressa)
stima=M.predict(regressore)
print(M.score(regressore, regressa))

plt.figure()
plt.plot(S["MOTHER_EDU"],S["FATHER_EDU"],"ob")
plt.plot(S["MOTHER_EDU"], stima, color="red")
