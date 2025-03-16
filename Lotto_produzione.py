import random

# Questa funzione genera casualmente la quantità di prodotti da produrre
def genera_quantita_produzione():
    prodotti = {
        "Pompe": random.randint(10, 100),  # Quantità tra 10 e 100
        "Trivelle": random.randint(5, 100),   # Quantità tra 5 e 100
        "Compressori": random.randint(8, 150)    # Quantità tra 8 e 150
    }
    return prodotti