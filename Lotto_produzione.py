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
