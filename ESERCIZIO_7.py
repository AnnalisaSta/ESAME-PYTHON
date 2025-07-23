#
# File: ESERCIZIO_7.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: ESERCIZIO_7
#
#

import matplotlib.pyplot as plt
import numpy as np

class Integral:
    """l'intervallo di integrazione è definito dalla tupla [a,b] e il nome della funzione è opzionale, altrimenti di default è 'funzione"""
    def __init__ ( self, Interval, function, name = 'funzione' ):
        self.I = Interval #intervallo di integrazione
        self.f = function #funzione da integrare
        self.fig, self.axes = plt.subplots ( nrows=2, ncols=1 ) #crea una figura con 2 grafici
        self.name = name #nome della funzione
    
    @staticmethod
    def R_sum ( I, N, f ):
        """calcola l'integrale mediante il metodo dei trapezi"""
        larghezza = ( I[1] - I[0] ) / N #calcola la larghezza di ogni intervallo
        
        somma = -f(I[0]) #inizializza la somma
        for x in np.linspace ( I[0], I[1], N, endpoint = False ): #calcola la somma delle altezze dei rettangoli
            somma += f(x) # somma delle basi del trapezio
    
        somma *= 2 #per la regola del trapezio la somma viene raddoppiata
        somma += f(I[0]) + f(I[1]) 
        somma /= 2 #viene fatta la media
        somma *= larghezza # moltiplicando per l'altezza del trapezio

        return somma #restituisce l'approssimazione

    def Compute ( self, N_iniziale:int, N_max:int, epsilon:float ):
        result = self.R_sum ( self.I, N_iniziale, self.f )
        while ( N_iniziale < N_max-1 ):
            N_iniziale+=1
            temp = self.R_sum ( self.I, N_iniziale, self.f )
    
            if abs ( ( result - temp ) ) < epsilon:
                result = temp
                break

            result = temp
            N_iniziale+=1
        
        return ( result, N_iniziale )

    def Print ( self, N_iniziale, N_finale, valore ) -> None:

        # initial step
        x = np.linspace ( self.I[0], self.I[1], N_iniziale )
        y = [ self.f(x_1) for x_1 in x ]
        self.axes[0].plot (x,y)

        xv = [ i for i,j in zip(x,y) if j > valore ]
        yv = [ j for i,j in zip(x,y) if j > valore ]
        self.axes[1].plot (xv,yv)

        # initial step
        x = np.linspace ( self.I[0], self.I[1], int( ( N_finale + N_iniziale ) / 2 ) )
        y = [ self.f(x_1) for x_1 in x ]
        self.axes[0].plot (x,y)

        xv = [ i for i,j in zip(x,y) if j > valore ]
        yv = [ j for i,j in zip(x,y) if j > valore ]
        self.axes[1].plot (xv,yv)

        # initial step
        x = np.linspace ( self.I[0], self.I[1], N_finale )
        y = [ self.f(x_1) for x_1 in x ]
        self.axes[0].plot (x,y)

        xv = [ i for i,j in zip(x,y) if j > valore ]
        yv = [ j for i,j in zip(x,y) if j > valore ]
        self.axes[1].plot (xv,yv)
 
        self.fig.savefig(f'{self.name}.png')#salva l'immagine in formato png



f = lambda x : (1/(np.sqrt(2*np.pi))) * np.exp (-0.5*pow(x,2)) 
g = lambda x : np.sin ( 10 / pow ( x, 2 ) ) if x != 0 else 0
h = lambda x : x*x

#parametri di integrazione
Interval = [-4,4]
N_default = 9 #numero di divisioni iniziali
epsilon = 0.001 #precisione richiesta
valore = 0.10 

if __file__ == "__main__" or True:
    N_max = int ( input ( "Quando vuoi essere sicuro ( N > 42 ) " ) )
    
    # create gli oggetti per ogni funzione 
    F = Integral ( Interval, f, 'f' )
    G = Integral ( Interval, g, 'g' )
    H = Integral ( Interval, h, 'h' )

    #calcola gli intgrali
    F_i, F_n = F.Compute ( N_default, N_max, epsilon )
    G_i, G_n = G.Compute ( N_default, N_max, epsilon )
    H_i, H_n = H.Compute ( N_default, N_max, epsilon )

    #stampa i risultati
    print ( f"L'integrale della funzione F è quasi {F_i} con N: {F_n}" )
    print ( f"L'integrale della funzione G è quasi {G_i} con N: {G_n}" )
    print ( f"L'integrale della funzione H è quasi {H_i} con N: {H_n}" )

    #genera e salva i grafici
    F.Print ( N_default, F_n, valore )
    G.Print ( N_default, G_n, valore )
    H.Print ( N_default, H_n, valore )
