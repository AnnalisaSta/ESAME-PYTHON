#
# File: ESERCIZIO_3.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: ESERCIZIO 3
#
#COMPLETO

import sys
import argparse
parser =  argparse.ArgumentParser()
parser.add_argument('-stampa_rubrica', action='store_true', help= 'se chiamato stampa la rubrica') #richiesta 7.1
parser.add_argument('-lista_età', action='store_true', help= 'se chiamato stampa la lista delle età in ordine crescente') #richiesta 7.2
parser.add_argument('-lista_invertita', action='store_true', help= 'se chiamato stampa la lista precedente in ordine invertito') #richiesta 7.3
parser.add_argument('-messaggio', action='store_true', help= 'se chiamato stampa il messaggio') #richiesta 7.4
parser.add_argument('-rubrica', action='store_true', help= 'se chiamato visualizza gli elementi della rubrica riferiti ad una chiave fornita come input') #richiesta 7.5

parser.add_argument('-c', '--chiave', help='stampa i valori relativi alla chiave')
parser.add_argument('-n', '--nome', help='nome della persona di cui stampare il messaggio')
args = parser.parse_args()

rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 89,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 43, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 19, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 54, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}


#richiesta 1: stampare delle stringhe formattate
if args.stampa_rubrica == True: #richiesta 7
    for nome, dati in rubrica.items():
        print(f"{nome}, {dati['giorno']}, {dati['mese']}, {dati['anno']}, {dati['età']}, {dati['sesso']}, {dati['mail']},")


#richiesta 2: a partire dalla rubrica, costruire la lista delle età, ordinata in ordine crescente e visualizzate i nomi in ordine crescente di età
if args.lista_età == True: #richiesta 7
    lista_età = []
    for dati_persona in rubrica.values(): #ogni dizionario interno alla rubrica viene chiamato dati_persona 
        lista_età.append(dati_persona['età']) #viene preso il valore si età e viene aggiunto alla lista_età
    lista_età.sort() #ordina la lista
    print(lista_età)

#richiesta 3: invertire i valori della lista precedente
if args.lista_invertita == True: #richiesta 7
    lista_età = []
    for dati_persona in rubrica.values(): #ogni dizionario interno alla rubrica viene chiamato dati_persona 
        lista_età.append(dati_persona['età']) #viene preso il valore si età e viene aggiunto alla lista_età
    lista_età.sort() #ordina la lista
    lista_età.reverse() #inverte l'ordine della lista
    print(lista_età)

#richiesta 4: 
if args.messaggio == True: #richiesta 7
    for nome, dati_persona in rubrica.items():
        sesso = dati_persona['sesso']
        if sesso == 'M': #determina il sesso della persona
            saluto = "Caro"
            nato = "nato"
        else:
            saluto = "Cara"
            nato = "nata"
            
        print(f"""{saluto} {nome},
    sei {nato} il {dati_persona['giorno']} di {dati_persona['mese']} del {dati_persona['anno']} e quindi a breve compirai {dati_persona['età']} anni.
    Ti manderemo gli auguri a {dati_persona['mail']}""")

#richiesta 5: Utilizzando args passare in input al programma una chiave e visualizzare tutti i valori corrispondenti a questa chiave
if args.rubrica ==  True: #richiesta 7
    chiave = args.chive
    for nome in rubrica:
        sottorubrica = rubrica[nome]
        for k in sottorubrica:
            if k == chiave:
                print(sottorubrica[k])

#richiesta 6: utilizzando argparse visualizzare la striga al punto 4 solo per il nome fornito come opzione al vostro programma
#funzione messaggio
nome_p = args.nome
for nome, dati_persona in rubrica.items():
    if nome == nome_p:
        sesso = dati_persona['sesso']
        if sesso == 'M': #determina il sesso della persona
            saluto = "Caro"
            nato = "nato"
        else:
            saluto = "Cara"
            nato = "nata"
            
        print(f"""{saluto} {nome},
    sei {nato} il {dati_persona['giorno']} di {dati_persona['mese']} del {dati_persona['anno']} e quindi a breve compirai {dati_persona['età']} anni.
    Ti manderemo gli auguri a {dati_persona['mail']}""")