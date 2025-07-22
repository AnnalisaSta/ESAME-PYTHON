#
# File: ESERCIZIO_6.py
#
# Author: A. Stantic
#
# Date: 23/07/2025
#
# Version: 1.0
#
# Description: ESERCIZIO 6
#
#

import json

class Rubrica:
    def __init__(self, dati_persona: dict ):
        self.dati_persona = dati_persona
        self.rubrica_aperta = True

    @classmethod
    def apri_da_json(cls, file_name):
        try: 
            file_json = open(file_name, 'r') #legge il file
            data = json.load(file_json)
            return cls(data)
        except FileNotFoundError:
                    print("File {file_name} non trovato.")
                    return cls({})    
    @classmethod
    def apri_da_txt(cls, file_name):
        try: 
            file_testo = open(file_name, 'r')
            data = {}
            for linea in file_testo:                                      
                valori = linea.split(',')              
                nome  = valori[0]
                giorno = valori[1]
                mese   = valori[2]
                anno   = valori[3]
                età    = valori[4]
                sesso  = valori[5]
                mail   = valori[6]
                data[nome] = {
                    'giorno': giorno,
                    'mese': mese,
                    'anno': anno,
                    'età': età,
                    'sesso': sesso,
                    'mail': mail
                }
        except FileNotFoundError:
            print("File {file_name} non trovato.")
            return cls({})
        return cls(data)

    def aggiungi(self, nome, info):
        if not self.rubrica_aperta:
                    print("Prima apri una rubrica")
                    return
        self.dati_persona[nome] = info
    
    def rimuovi(self, nome):
            if not self.dati_persona:
                print("La rubrica è vuota")
                return
            if nome in self.dati_persona:
                del self.contatti[nome]
            else:
                print(f"Il contatto {nome} non esiste in rubrica")
    def salva(self, filename):
            if not self.dati_persona:
                print("La rubrica è vuota")
                return
            try:
                if filename.lower().endswith('.json'):
                    with open(filename, 'w') as file:
                        #indent=4, ogni livello della struttura JSON verrà rientrato di 4 spazi
                        #mantenere i caratteri speciali òàù...
                        json.dump(self.dati_persona, file, indent=4,ensure_ascii=False) #indent=4, ogni livello della struttura JSON verrà rientrato di 4 spazi
                else:
                    with open(filename, 'w') as file:
                        for nome, info in self.dati_persona.items():
                            valori = [str(v) for v in info.values()]
                            nuova_riga = f"{nome}, {', '.join(valori)}\n"
                            file.write(nuova_riga)
            except Exception as e:
                print(f"Errore durante il salvataggio: {e}")
            file.close()
                    
    def stampa(self, nome):
        if not self.dati_persona:
            print('la rubrica è vuota')
            return
        if nome in self.dati_persona:
            print(f"Dati di {nome}:")
            dati = self.dati_persona[nome]
            for chiave, valore in dati.items():
                print(f'{chiave}: {valore}')
        else:
            print('Non ci sono i dati di ', nome)
    
    