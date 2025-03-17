# Traccia-1.5-UniPegaso
# Project Work Università Telematica UniPegaso

## Introduzione
Questo repository contiene i materiali relativi al project work finale del Corso di Laurea L-31 "Informatica per le Aziende Digitali". La traccia scelta è la 1.5: "Sviluppo di un codice python per simulare un processo produttivo nel settore secondario".

Titolo del progetto: "Simulazione della Produzione Industriale: Un’Analisi con Python".

Dal punto di vista tecnico, il progetto prevede lo sviluppo di un codice Python con i seguenti obiettivi:

Implementare una funzione per generare casualmente le quantità di produzione per almeno tre tipologie di prodotto.
Creare una funzione per la generazione casuale dei parametri di configurazione, inclusi il tempo di produzione per unità e per tipologia di prodotto, la capacità massima di produzione giornaliera per ciascun prodotto e la capacità produttiva complessiva.
Calcolare e restituire il tempo totale necessario per completare l'intero lotto di produzione.

## Implementazioni
Sono state implementate le seguenti funzioni rispetto a quanto richiesto dal Project Work, per rendere il codice più funzionale e accurato.

Controllo sulla capacità produttiva massima giornaliera: verifica se il tempo totale di produzione supera il limite di 1440 minuti (24 ore) e avvisa l'utente se è necessario distribuire il carico su più giorni.
Stampa dettagliata delle quantità da produrre: mostra il numero di unità generate casualmente per ogni prodotto.
Stampa dettagliata dei parametri di produzione: include il tempo per unità e la capacità massima giornaliera per ogni prodotto.
Stampa dettagliata del calcolo del tempo di produzione: visualizza il tempo richiesto per ogni prodotto in base alla quantità e al tempo per unità.
Conversione del tempo totale in ore e minuti: rende l'output più leggibile invece di lasciare il valore solo in minuti.

## Prerequisiti
Per garantire il corretto funzionamento del codice, è necessario installare Python:

Python: Può essere scaricato per tutti i comuni sistemi operativi dal sito ufficiale https://www.python.org/downloads/

Successivamente, apri il terminale e spostati in una cartella a scelta per scaricare i file di progetto, contenuti nella cartella Traccia1.5, utilizzando il comando seguente: git clone https://github.com/GiuseppeBerardi97/Traccia-1.5-UniPegaso.git

In alternativa al comando git clone, puoi scaricare l'intero progetto in formato .zip e decomprimerlo una volta completato il download. Per farlo, clicca sul tasto "Code" in alto e nel menu che si apre seleziona "Download ZIP".

## Esecuzione
Per poter eseguire correttamente il codice, aprire il terminale del proprio Sistema Opoerativo 
Spostarsi all'interno della cartella clonata del progetto contenente tutti i file necessari.

All'interno della cartella saranno presenti i seguenti file:

- "README.md"
- "Lotto_produzione.py"

Succesivamente, andrà eseguito il codice con il comando:
> python3 <NOME_CODICE>.py
Nel caso di errore relativamente al comando verificare che il path sia giusto.
