#
# File: PROGETTO_FINALE.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: chiede una data e stampa i tempi fatti e il luogo salvati in un file json
#
#

import json

class RisultatiGare:
    def __init__(self, dati: dict):
        self.dati = dati
        self.risultati_aperti = True #assegna il valore boolenao all'attributo
    
    @classmethod
    def apri_da_json(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file_json:#utf-8 salva accenti
                dati = json.load(file_json)
            return cls(dati)
        except FileNotFoundError:
            print("File {filename} non trovato.")
            return cls({})


    def aggiungi(self, data, tempo, luogo):
        if not self.risultati_aperti:
            print("Prima apri un file di risultati")
            return

        nuovo_risultato = {"tempo": tempo, "luogo": luogo}
        if data in self.dati:
            #se data trovata, aggiungi nuovo risultato in coda alla lista
            self.dati[data].append(nuovo_risultato)
        else:
            self.dati[data] = [nuovo_risultato]

    def stampa(self, data):
        if not self.dati:
            print("nessun risultato disponibile")
            return
        if data not in self.dati:
            print(f"Nessun risultato per la data: {data}")
            return

        print(f"Risultati per il {data}:")
        for i, risultato in enumerate(self.dati[data], start=1):
            print(f"  Gara {i}: Tempo = {risultato['tempo']}, Luogo = {risultato['luogo']}")

    def salva(self, filename):
        if not self.dati:
            print("Nessun dato da salvare")
            return
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.dati, file, indent=4, ensure_ascii=False)

    def rimuovi(self, data):
        if not self.dati:
            print("Nessun risultato presente")
            return
        if data not in self.dati:
            print(f"La data {data} non esiste nei risultati")
            return
        del self.dati[data]
        print(f"Risultati del {data} rimossi con successo")



#permette di modificare le gare
def main():
    gare = RisultatiGare.apri_da_json('gare.json')

    data_f = input("Inserire una data (es. 24/06/2023) o 'esci' per terminare: ").strip().lower()
    gare.stampa(data_f)


    filename = "gare.json"
    gare = RisultatiGare.apri_da_json(filename)

    print("---Aggiungi nuovo risultato gara---".upper())
    data = input("Inserisci la data (gg/mm/aaaa): ")
    tempo = input("Inserisci il tempo (es. 11.23): ")
    luogo = input("Inserisci il luogo: ")

    gare.aggiungi(data, tempo, luogo)
    gare.salva(filename)

    print("Risultato aggiunto con successo!")


if __name__ == "__main__":
    main()




