# Cinema Aurora 🎬

**Cinema Aurora** è un'applicazione web sviluppata in Python con Flask per la gestione di un cinema. Il sistema permette agli utenti di consultare i film in programmazione, esplorare le sale e visualizzare gli incassi.

Per ogni film è possibile visualizzare le informazioni dettagliate, la trama e gli spettacoli disponibili per ogni sala. Inoltre, per ciascuno spettacolo è presente un pulsante per accedere ai dettagli e ai biglietti, dove l'utente può controllare la data, l'ora, la sala, il prezzo e i posti disponibili, effettuando l'acquisto e vedendo i posti liberi aggiornarsi immediatamente.
Per ogni sala è possibile consultare la capienza massima e la lista degli spettacoli in programma. 
Nell'area degli incassi vengono mostrati il totale dei biglietti venduti, l'incasso complessivo e il film più visto, accompagnati da una tabella riassuntiva degli incassi per singolo film e da una tabella sul livello di riempimento delle sale.

---

## Team di Sviluppo
Il progetto è stato realizzato in collaborazione da:
- **Aurora**
- **Claudia**
- **Roberto**

---

## Tecnologie Utilizzate
- **Backend**: Python, Flask
- **Database**: MySQL
- **Frontend & UI**: HTML, CSS, Bootstrap
- **Template Engine**: Jinja2 (con ereditarietà dei layout, cicli e condizioni dinamiche)
- **Versioning**: Git & GitHub (flusso basato su branch dedicati e Pull Request)

---

## Funzionalità Principali
1. **Home Page**: Visualizzazione di tutti i film attualmente in programmazione con locandina, genere e durata.
2. **Dettagli Film**: Scheda informativa approfondita con regista, genere, trama e la lista degli spettacoli associati.
3. **Gestione Sale**: Panoramica delle sale (*Sala Verde*, *Sala Blu*, *Sala Studio*, *Sala Odeon*) con stili visivi personalizzati, capienza totale e spettacoli programmati.
4. **Acquisto Biglietti**: Interazione utente guidata tramite modale di conferma ("Sì/No") con alert dinamici a scomparsa e gestione in tempo reale dei posti liberi/occupati.
5. **Area Incassi e Statistiche**: Dashboard con il totale dei biglietti venduti, l'incasso complessivo, il film più visto, una tabella con i film ordinati per incasso maggiore e una tabella con la percentuale di riempimento degli spettacoli.

---

## Struttura del Database
Il database relazionale denominato `cinema` gestisce le seguenti tabelle:
- **`biglietti`**: Storico degli acquisti effettuati per ciascuno spettacolo.
- **`film`**: Informazioni su titoli, registi, generi, durata, trama e locandine.
- **`sale`**: Elenco delle sale con la capienza massima in termini di posti.
- **`spettacoli`**: Programmazione che collega film e sale con data, ora e prezzo.

---

## Istruzioni per l'Avvio in Locale
1. Clona il repository Git:
   ```bash
   git clone [https://github.com/auror-web/CinemaAurora.git](https://github.com/auror-web/CinemaAurora.git)
   ```

2. Spostati nella cartella del progetto e attiva il tuo ambiente virtuale (venv).

3. Installa le dipendenze richieste con:
    ```bash
    pip install flask mysql-connector-python
    ```

4. Configura il database MySQL in locale (cinema) utilizzando gli script SQL predisposti.

5. Avvia l'applicazione Flask:
    ```bash
    python app.py
    ```