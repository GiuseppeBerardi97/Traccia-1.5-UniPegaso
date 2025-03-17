import random

# Genera casualmente la quantità di prodotti da produrre 
# utilizzando il modulo random per assegnare un numero casuale di unità
# ad ogni tipo di prodotto all'interno di un range specifico
def genera_quantita_produzione():
    prodotti = {
        "Pompe": random.randint(2, 20),  # Quantità tra 2 e 20
        "Trivelle": random.randint(2, 15),   # Quantità tra 2 e 15
        "Compressori": random.randint(2, 30)    # Quantità tra 2 e 30
    }
    return prodotti

# Questa funzione genera i parametri di produzione casualmente all'interno del range imposto
def genera_parametri_produzione():
    parametri = {
        "Pompe": {
            "tempo_per_unita_min": 25,  # Tempo minimo per unità (25 minuti)
            "tempo_per_unita_max": 45,  # Tempo massimo per unità (45 minuti)
            "capacita_massima_giornaliera": random.randint(15, 50)  # Capacità massima giornaliera
        },
        "Trivelle": {
            "tempo_per_unita_min": 35,  # Tempo minimo per unità (35 minuti)
            "tempo_per_unita_max": 40,  # Tempo massimo per unità (40 minuti)
            "capacita_massima_giornaliera": random.randint(10, 40)  # Capacità massima giornaliera
        },
        "Compressori": {
            "tempo_per_unita_min": 55,  # Tempo minimo per unità (55 minuti)
            "tempo_per_unita_max": 80,  # Tempo massimo per unità (80 minuti)
            "capacita_massima_giornaliera": random.randint(20, 60)  # Capacità massima giornaliera
        },
        "Capacita_Complessiva": 1440  # Massimo 24 ore (1440 min) su 3 turni da 8 ore
    }
    
    # Calcolo della somma delle capacità massime giornaliere
    somma_capacita_massima = sum(parametri[prodotto]["capacita_massima_giornaliera"] for prodotto in parametri if prodotto != "Capacita_Complessiva")
    
    return parametri, somma_capacita_massima

# Calcola il tempo totale di produzione in minuti, considerando tempi variabili per ogni unità di prodotto e restituisce i dettagli della produzione
# con il tempo per ogni unità prodotta in una lista di stringhe
def calcola_tempo_totale_produzione(quantita, parametri):
    tempo_totale = 0
    dettagli_produzione = []
    
    for prodotto in quantita:
        if prodotto == "Trivelle":
            # Per ogni unità di trivella, il tempo per unità è casuale
            for i in range(quantita[prodotto]):
                tempo = random.randint(parametri[prodotto]["tempo_per_unita_min"], parametri[prodotto]["tempo_per_unita_max"])
                tempo_totale += tempo
                dettagli_produzione.append(f"{prodotto} {i+1}: {tempo} min")
        elif prodotto == "Pompe":

            # Per ogni unità di pompa, il tempo per unità è casuale
            for i in range(quantita[prodotto]):
                tempo = random.randint(parametri[prodotto]["tempo_per_unita_min"], parametri[prodotto]["tempo_per_unita_max"])
                tempo_totale += tempo
                dettagli_produzione.append(f"{prodotto} {i+1}: {tempo} min")
        elif prodotto == "Compressori":
            
            # Per ogni unità di compressore, il tempo per unità è casuale
            for i in range(quantita[prodotto]):
                tempo = random.randint(parametri[prodotto]["tempo_per_unita_min"], parametri[prodotto]["tempo_per_unita_max"])
                tempo_totale += tempo
                dettagli_produzione.append(f"{prodotto} {i+1}: {tempo} min")
    
    return tempo_totale, dettagli_produzione


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

  # Calcolo delle ore e minuti
    ore = tempo_totale_minuti // 60
    minuti = tempo_totale_minuti % 60

    print(f"\nIl tempo totale complessivo è: {tempo_totale_minuti} minuti ({ore} ore e {minuti} minuti)")

    # Verifica se il tempo totale supera la capacità complessiva giornaliera
    if tempo_totale_minuti > parametri["Capacita_Complessiva"]:
        print("\nATTENZIONE: La produzione totale supera il limite di 24 ore. È necessario distribuire il carico di lavoro su più giorni.")
    else:
        print("\nLa produzione rientra nel limite giornaliero di 24 ore.")
