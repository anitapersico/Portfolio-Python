# -*- coding: utf-8 -*-
"""
BiblioSoftware - Soluzione Integrata per la Gestione delle Biblioteche
Software CLI per la gestione dell'inventario, dei prestiti e delle statistiche di una biblioteca.
"""

# Dizionario con l'inventario iniziale dei libri e le relative copie
inventario = {
    "Cime tempestose": 5,
    "Circe": 7,
    "Orgoglio e pregiudizio": 8,
    "After": 3
}

# Funzione per aggiungere un libro o aumentarne le copie
def aggiungi_libro(titolo, copie):
    if (titolo in inventario):
        inventario[titolo] += copie
        print(f"il libro {titolo} è stato aggiornato: ora a stock ci sono {inventario[titolo]} copie")
    else:
        inventario[titolo] = copie
        print(f"il libro {titolo} è stato aggiunto al sistema con {copie} copie")

# Funzione per rimuovere un libro
def rimuovi_libro(titolo):
    if (titolo in inventario):
        del inventario[titolo]
        print(f"il libro {titolo} è stato eliminato")
    else:
        print(f"errore, il libro {titolo} non esiste")

# Funzione per verificare se un libro è disponibile
def verifica_disponibilita(titolo):
    if (titolo in inventario and inventario[titolo] > 0):
        print(f"sono disponibili {inventario[titolo]} copie del libro {titolo}")
        return True
    else:
        print(f"il libro {titolo} non è disponibile")
        return False

# Funzione per prendere in prestito una copia di un libro
def prendi_in_prestito(titolo):
    if (titolo in inventario and inventario[titolo] > 0):
        inventario[titolo] -= 1
        print(f"è stato preso in prestito di una copia del libro {titolo}. copie disponibili al momento:{inventario[titolo]}")
    else:
        print(f"errore, il libro {titolo} non esiste")

# Funzione per calcolare le statistiche della biblioteca
def statistiche_biblioteca():
    totale_libri = len(inventario)

    # Controllo per evitare la divisione per zero se la biblioteca è vuota
    if (totale_libri) == 0:
        return {"totale_libri": 0, "copie_totali": 0, "media_copie": 0}

    copie_totali = sum(inventario.values())
    media_copie = copie_totali / totale_libri

    return {
        "totale_libri": totale_libri,
        "copie_totali": copie_totali,
        "media_copie": media_copie
    }

# Funzione per mostrare tutti i libri disponibili
def visualizza_libri():
    if (len(inventario) > 0):
        for titolo, copie in inventario.items():
            print(f"{titolo}:{copie} copie")
    else:
        print("errore, nella biblioteca non ci sono libri")

# Funzione per aggiungere copie a un libro già esistente
def restaurare_libro(titolo, copie):
    if (titolo in inventario):
        inventario[titolo] += copie
        print(f"il libro {titolo} è stato aggiornato, copie: {copie}")
    else:
        print(f"errore, il libro {titolo} non esiste")

# Ciclo principale per interagire con l'utente
while True:
    print("1. aggiungi libro")
    print("2. rimuovi libro")
    print("3. verifica disponibilità")
    print("4. prendi in prestito")
    print("5. statistiche")
    print("6. visualizza libri")
    print("7. restaura libro")
    print("8. esci")

    opzione = input("Scegli un'opzione (numero):")

    if (opzione == "1"):
        titolo = input("Quale libro vuoi aggiungere?")
        copie = int(input("Quante copie?"))
        aggiungi_libro(titolo, copie)

    elif (opzione == "2"):
        titolo = input("Quale libro vuoi rimuovere?")
        rimuovi_libro(titolo)

    elif (opzione == "3"):
        titolo = input("Di quale libro vuoi verificare la disponibilità?")
        verifica_disponibilita(titolo)

    elif (opzione == "4"):
        titolo = input("Quale libro vuoi prendere in prestito?")
        prendi_in_prestito(titolo)

    elif (opzione == "5"):
        print(statistiche_biblioteca())

    elif (opzione == "6"):
        visualizza_libri()

    elif (opzione == "7"):
        titolo = input("Quale libro vuoi restaurare? ")
        copie = int(input("Quante copie da aggiungere? "))
        restaurare_libro(titolo, copie)

    elif (opzione == "8"):
        print("Programma terminato.")
        break
    else:
        print("opzione non riconosciuta")

