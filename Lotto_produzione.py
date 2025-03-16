import random

# Questa funzione genera casualmente la quantità di prodotti da produrre
def genera_quantita_produzione():
    prodotti = {
        "Pompe": random.randint(10, 100),  # Quantità tra 10 e 100
        "Trivelle": random.randint(5, 100),   # Quantità tra 5 e 100
        "Compressori": random.randint(8, 150)    # Quantità tra 8 e 150
    }
    return prodotti

# Questa funzione genera i parametri di produzione casualmente all'interno del range imposto
def genera_parametri_produzione():
    parametri = {
        "Pompe": {
            "tempo_per_unita": random.randint(3, 8),  
            "capacita_massima_giornaliera": random.randint(50, 200)  
        },
        "Trivelle": {
            "tempo_per_unita": random.randint(5, 10),  
            "capacita_massima_giornaliera": random.randint(30, 150)  
        },
        "Compressori": {
            "tempo_per_unita": random.randint(4, 9),  
            "capacita_massima_giornaliera": random.randint(40, 180)  
        },
        "Capacita_Complessiva": 1440  # Massimo 24 ore (1440 min) su 3 turni da 8 ore
    }
    
    # Calcolo della somma delle capacità massime giornaliere
    somma_capacita_massima = sum(parametri[prodotto]["capacita_massima_giornaliera"] for prodotto in parametri if prodotto != "Capacita_Complessiva")
    
    return parametri, somma_capacita_massima

# Funzione per calcolare il tempo totale di produzione in minuti
def calcola_tempo_totale_produzione(quantita, parametri):
    return sum(quantita[prodotto] * parametri[prodotto]["tempo_per_unita"] for prodotto in quantita)

if __name__ == "__main__":
    quantita = genera_quantita_produzione()
    parametri, somma_capacita_massima = genera_parametri_produzione()
    
    print("Quantità giornaliera richiesta da produrre:")
    for prodotto, qta in quantita.items():
        print(f"{prodotto}: {qta}")
    
    print("\nParametri di produzione (tempo in minuti):")
    for prodotto, param in parametri.items():
        if prodotto != "Capacita_Complessiva":
            print(f"{prodotto} - Tempo per unità: {param['tempo_per_unita']} min, Capacita massima giornaliera: {param['capacita_massima_giornaliera']}")
        else:
            print(f"\nCapacita complessiva giornaliera: {param} minuti (massimo 24 ore)")

    print(f"\nSomma delle capacità massime giornaliere dei prodotti: {somma_capacita_massima} unità")

    tempo_totale_minuti = calcola_tempo_totale_produzione(quantita, parametri)
    
    print("\nRiepilogo della produzione:")
    for prodotto in quantita:
        tempo_prodotto_minuti = quantita[prodotto] * parametri[prodotto]['tempo_per_unita']
        print(f"{prodotto}: {quantita[prodotto]} unità x {parametri[prodotto]['tempo_per_unita']} min per unità = {tempo_prodotto_minuti} minuti")
