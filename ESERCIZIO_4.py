#
# File: ESERCIZIO_4.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: ESERCIZIO 4
#
#COMPLETO

import json #si importa il modulo per creare i file di tipo JSON
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

#rihiesta 1: aggiungere un'opzione al programma per generare un file di testo rubrica.txt
with open("rubrica.txt", "w") as f:
    for nome, dati in rubrica.items():
        riga = f"{nome},{dati['giorno']},{dati['mese']},{dati['anno']},{dati['età']},{dati['sesso']},{dati['mail']}"
        f.write(riga + '\n')

        
#richiesta 2: creare un file JSON contentente la rubrica con la stessa struttura del dizionario interno al programma
with open("rubrica.json", "w") as file_json: #scrive il contenuto del dizionario nel file object
    json.dump(rubrica, file_json, indent= 4) #scrive il contenuto del dizionario nel file e l'indentazione è necessaria per dargli la forma corretta

#richiesta 3: leggera la rubrica salvata in un file formato JSON  e visualizzarne tutto il contenuto
with open('rubrica.json', 'r') as in_file:
    data = json.load(in_file) #legge il contenuto del file
print(data) #stampa i contenuti