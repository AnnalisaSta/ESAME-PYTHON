#
# File: ESERCIZIO_2.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: ESERCIZIO 2
#
#COMPLETO

testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

#richiesta 1 : contare le righe del testo escludendo gli spazi
lista_righe = testo.splitlines() #la funzione .splitlines() permette di dividere il testo in più righe
x = 0
for riga in lista_righe:
    if riga != "":
        x += 1
print('Numero di righe:', x)

#richiesta 2: contare le parole del testo
lista_parole = testo.split() #la funzione .split() utilizza gli spazi per dividere il testo in parole
x = 0
for parola in lista_parole:
    x += 1
print('Numero di parole:', x)

#richiesta 3: contare i caratteri del testo
x = len(testo) #la funzione len() conta tutti i caratteri, compresi gli spazi
print('Numero di caratteri:', x)

#richiesta 4: sostituite le parole day, water e about con la parola PYTHON in tutti i versi
lista_parole = testo.split() #divide il testo in parole
lista_nuova = []
for parola in lista_parole:
    parola = parola.strip(',.;:!')
    parola = parola.lower()
    if parola != 'day' and parola != 'water' and parola != 'about':
        lista_nuova.append(parola)
    else:
        lista_nuova.append('PYTHON')
print(lista_nuova)

#richiesta 5: riscrivete il testo con tutte le parole in posizione dispari scritte in maiuscolo
lista_parole = testo.split() #divide il testo in parole
lista_nuova = []
x = 1
for parola in lista_parole:
    x = x + 1
    if x %2 == 0: # se il resto della divisione per il numero 2 è 0
        lista_nuova.append(parola) #si aggiunge la parola alla lista_nuova
    else:
        lista_nuova.append(parola.upper()) #altrimenti si aggiunge la parola scritta in maiuscolo a lista_nuova
print(lista_nuova)

#richiesta 6: riscrivere il testo a specchio
caratteri = list(testo) #divide il testo in caratteri
caratteri.reverse() #riscrive i caratteri a specchio
testo_nuovo = ' '.join(caratteri) #riscrive il testo unendo i caratteri
print(testo_nuovo)

#richiesta 7: trovare parole che compaiono in tutte le strofe
lista_righe = testo.splitlines() #divide il testo in righe, ovvero quando trova \n
strofa_i = [] #lista di righe non vuote
lista_strofe = [] #lista che conterrà tutte le strofe
for riga in lista_righe:
    if riga == '':
        if strofa_i: #se la lista strofa_i contiene righe
            lista_strofe.append(strofa_i) #aggiungerla alla lista_strofe
            strofa_i = [] #si tolgono gli elementi dalla lista per iniziare la prossima
    else:
        strofa_i.append(riga)
if strofa_i: #per chiudere la lista se il testo non termina con una riga vuota
    lista_strofe.append(strofa_i)

#richiesta 8: creare una lista di tutte le parole e ordinarle in base alla lunghezza 
testo = testo.lower() #riscrive il testo in lettere minuscole
lista_parole = testo.split() #divide il testo in parole
lista_parole.sort(key=len) #si ordinano le parole in base alla lunghezza
print(lista_parole)

#richiesta 9: creare un dizionario che ad ogni carattere associa la sua occorenza nel testo
testo = testo.lower() #riscrive tutto il testo in lettere minuscole in modo da considerare ogni volta che la lettera si ripete
dizionario = {} #si crea un dizionario vuoto
for carattere in testo: #si considerano tutti i caratteri presenti nel testo
    if carattere in dizionario: #se il carattere è già presente nel dizionario
        dizionario[carattere] += 1 #si incrementa di uno il suo valore
    else:
        dizionario[carattere] = 1 #altrimenti gli si assegna il valore 1
print(dizionario)

#richiesta 10: creare un dizionario come il precedente e contare le lettere
testo = testo.lower() #si riscrive il testo in minuscolo
dizionario = {}  #si crea un dizionario vuoto
for carattere in testo:
    if carattere.isalpha():  #se il carattere è una lettera
        if carattere in dizionario: #se la lettera è già presente nel dizionario
            dizionario[carattere] += 1 #incrementare il suo valore di 1
        else:
            dizionario[carattere] = 1 #se non è presente nel dizionario assegnarle il valore 1
print(dizionario)
