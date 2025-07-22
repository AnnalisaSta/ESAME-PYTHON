#
# File: ESERCIZIO_8.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: ESERCIZIO 8
#
#COMPLETO

#richiesta 1: scrivere il programma con un approccio LBYL
import json
import random

with open('impiccato.json', 'r') as file: #si fa leggere il file json salvato
    parole = json.load(file) #carica su python la lista di parole dal file json

parola = random.choice(parole) #sceglie casualmente una parola dalla lista
parola.lower() #trasforma la parola in una parola in lettere minuscole
parola_nascosta = [] #si definisce la parola_nascosta come una lista vuota
for lettera in parola:
    parola_nascosta.append('_') #per ogni lettera della parola si aggiunge _ alla lista creata
lettere_indovinate = set() #si crea un set i cui elementi sono le lettere già trovate
tentativi_max = 10 #si fornisce un numero di tentativi massimo
tentativi = 0 #contatore per il numero di tentativi

print("La parola da indovinare ha:", "len(parola) lettere")

while tentativi < tentativi_max and '_' in parola_nascosta: #il ciclo si ripete dino a quando non si è superato il limite di tentativi e _ sono ancora presenti nella lista
    print("\nParola corrente:", ' '.join(parola_nascosta))
    print(f"Tentativi rimasti: {tentativi_max - tentativi}") #indica il numero di tentativi
    lettera = input("Inserisci una lettera: ")
    lettera.lower()

    if lettera in parola: 
        print("La lettera è nella parola")
        for i in range(len(parola)):
            if parola[i] == lettera: #se la lettera è uguale all'elemento in i-esima posizione della lista
                parola_nascosta[i] = lettera #mettere in posizione i-esima in parola_nascosta la lettera

    if not lettera.isalpha() or len(lettera) > 1:
        print("inserire una sola lettera")
        continue

    if lettera in lettere_indovinate:
        print("lettera già usata")
        continue



    else:
        print("la lettera sbagliata")
        tentativi += 1

if '_' not in parola_nascosta: #se si ha trovato tutte le lettere
    print(f"\nil gioco è finito, la parola è: {parola}")
else: #se il numero di tentativi è finito
    print(f"\nhai perso, La parola era: {parola}")


#richiesta 2: scrivere il programma con un approccio EAFP
import json
import random

with open('impiccato.json', 'r') as file: #si fa leggere il file json salvato
    parole = json.load(file) #carica su python la lista di parole dal file json

parola = random.choice(parole) #sceglie casualmente una parola dalla lista
parola.lower() #trasforma la parola in una parola in lettere minuscole
parola_nascosta = [] #si definisce la parola_nascosta come una lista vuota
for lettera in parola:
    parola_nascosta.append('_') #per ogni lettera della parola si aggiunge _ alla lista creata
lettere_indovinate = set() #si crea un set i cui elementi sono le lettere già trovate
tentativi_max = 10 #si fornisce un numero di tentativi massimo
tentativi = 0 #contatore per il numero di tentativi

print("La parola da indovinare ha:", "len(parola) lettere")

while tentativi < tentativi_max and '_' in parola_nascosta: #il ciclo si ripete dino a quando non si è superato il limite di tentativi e _ sono ancora presenti nella lista
    print("\nParola corrente:", ' '.join(parola_nascosta))
    print(f"Tentativi rimasti: {tentativi_max - tentativi}") #indica il numero di tentativi
    lettera = input("Inserisci una lettera: ")
    lettera.lower()

    try:
        lettere_indovinate.add(lettera)
    except Exception:
        print('Il carattere aggiunto non è una lettera')

    if lettera in parola: 
        print("La lettera è nella parola")
        for i in range(len(parola)):
            if parola[i] == lettera: #se la lettera è uguale all'elemento nell'i-esima posizine della lista
                parola_nascosta[i] = lettera

    else:
        print("la lettera sbagliata")
        tentativi += 1

if '_' not in parola_nascosta: #se si ha trovato tutte le lettere
    print(f"\nil gioco è finito, la parola è: {parola}")
else: #se il numero di tentativi è finito
    print(f"\nhai perso, La parola era: {parola}")

    