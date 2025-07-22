#
# File: ESERCIZIO_5.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: ESERCIZIO 5
#
#

N = 8
def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    # distanza lungo y
    dy = abs(y1 - y0)
    
    # distanza lungo x
    dx = abs(x1 - x0) 

    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy     


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna 
      delle posizioni delle regine precedenti 
    '''
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):     
        # la coordinata X (la riga) è indice (c) 
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True  
    # nessun incrocio, la posizione va bene e NON incrocia altre colonne        
    return False   


def soluzione_ok(soluzione_posizioni):
    '''Controlla tutte le posizioni della possibile soluzione
       'soluzione_posizioni' per verificare se ognuna delle posizioni 
       (colonne dela permatazione) ogni colonna incrocia la diagonale
       di qualche altra posizione
    '''

    for col in range(1, len(soluzione_posizioni)):
        # verifica se incrocia
        #if incrocia_colonne(soluzione_posizioni, col) == True:
        if incrocia_colonne(soluzione_posizioni, col):
            # stop se trova incroci, la soluzione non è valida
            return False 

    # Se non è ritornato prima, 
    # allora nessun incrocio trovato: posizioni della soluzione valide 
    return True 

#richiesta 7: Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi. 
# Scrivere delle funzioni che, una volta trovata una soluzione alla scacchiera, costruiscano le 4 soluzioni simmetriche per rotazione.
# Trovate 10 soluzioni uniche e le rispettive simmetriche per una scacchiera 8x8
def centrate(soluzione): #funzione per spostare il centro della scacchiera da (4, 4) in (0, 0)
    return [(col - 4, riga - 4) for x, y in enumerate(soluzione)] 

def originali(coordinate):
    posizioni = []
    for _ in range(N): #crea una lista di tutti 0
        posizioni.append(0)
    for x, y in coordinate:
        riga = y + 4
        col = x + 4
        posizioni[riga] = col
    return posizioni

def ruota_90(coordinate):
    return [(-y, x) for x, y in coordinate]

def ruota_180(coordinate):
    return ruota_90(ruota_90(coordinate))

def ruota_270(coordinate):
    return ruota_90(ruota_180(coordinate))

def tutte_rotazioni(soluzione):
    """Ritorna tutte le rotazioni della soluzione come liste [col per riga]"""
    centrata = centrate(soluzione)
    return [
        originali(centrata),
        originali(ruota_90(centrata)),
        originali(ruota_180(centrata)),
        originali(ruota_270(centrata)),
    ]

import random
import time 

def main():
    # inizializzo generatore permutazioni
    random_generator = random.Random() 
    
    # preparo la "possibile soluzione" con posizoni da testare
    scacchiera = list(range(N)) #richiesta 5: permette di estendere il problema ad una scacchiera NxN
    
    # conto le soluzioni trovate, inizio da 0           
    solutions = 0                 
    
    lista_tempi = [] #richiesta 1: si crea una lista vuota contenente i tempi

    lista_u = [] #richiesta 3: lista delle soluzioni uniche

    lista_d = [] #richeista 3: lista delle soluzioni ripetute

    # misuro il tempo di partenza per la ricerca della soluzione
    start_time = time.time()            
    tentativi = 0 #richiesta 2: il numero di tentativi iniziali è 0
    # loop finchè non trovo una soluzione
    while solutions < 10: #richiesta 1: fornisce 10 soluzioni
        tentativi += 1 #richiesta 2: ogni volta che inizia il ciclo while il contatore incrementa di 1
        # permutazione casuale della soluzione 'mescolando' posizioni
        random_generator.shuffle(scacchiera) 
        
        # verifica se la permutazione casuale e' soluzione  
        #if soluzione_ok(scacchiera) == True: 
        if soluzione_ok(scacchiera):
            # se la soluzione è buona, scrive
            print(f'Found solution {scacchiera} in {time.time() - start_time} s.')

            #richiesta 1:
            lista_tempi.append(time.time() - start_time) #si aggiungono alla lista i tempi trovati
            tempo_medio = sum(lista_tempi) / len(lista_tempi) #si calcola il tempo medio come rapporto della somma di tutti gli elementi della lista e il numero di elementi della lista
            print(tempo_medio) #stampa il tempo medio per trovare le soluzioni
            

            #richiesta 2:
            print(f'Tentativi: {tentativi} ') #se si ha un risultato positivo stampa il numero di tentativi fatti
        

            #richiesta 3:
            if scacchiera not in lista_u: #se la soluzione non è nella lista delle soluzioni uniche
                lista_u.append(scacchiera) #aggiungerla a lista_u
            else:
                lista_d.append(scacchiera) #se è già presente aggiungerla nella lista delle soluzioni ripetute
            print(lista_u)

            # incremento contatore soluzioni trovate (condizione stop loop)
            solutions += 1
            
            start_time = time.time() # reset timer ricerca soluzione
            tentativi = 0 # reset contatore tentativi

#richiesta 6:
def trova_massimo_N_limite_tempo(max_seconds=30): #si può variare il tempo massimo, nella richiesta è 30s
    N = 4  # il valore minimo per cui si può trovare una soluzione è N = 4
    while True: #ciclo che aumente il valore di N fino a quando non vengono superati i 30s
        scacchiera = list(range(N))
        random_generator = random.Random()
        start_time = time.time()
        trovato = False
        tentativi = 0

        while time.time() - start_time < max_seconds:
            random_generator.shuffle(scacchiera)
            tentativi += 1
            if soluzione_ok(scacchiera):
                trovato = True
                break
        
        if not trovato:
            print(f"Tempo limite superato per N = {N}")
            return N - 1, tentativi
        else:
            print(f"Trovata soluzione per N = {N} in meno di {max_seconds}s (tentativi: {tentativi})")
        N += 1


massimo_N, tentativi = trova_massimo_N_limite_tempo()
print(f"Massimo N per cui è trovata almeno una soluzione in <30s: {massimo_N}")

main()
