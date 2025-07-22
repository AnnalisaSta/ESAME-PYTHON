#
# File: ESERCIZIO_7.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: ESERCIZIO 7
#
#


import numpy as np
import matplotlib.pyplot as plt
import sympy

#richiesta 1: calcolare l’integrale della funzione nell’intervallo campionando la funzione in un numero di punti massimo,
#selezionabile dall’utente, ma parta da un valore di default
x, y = symbols('x y') #si usa il modulo sympy per trasformare in simboli x e y