import mysql.connector
#Connessione
def connetti():
    return mysql.connector.connect(
        host="localhost",
        user="studente",
        password="studente",
        database="cinema"
    )

#Tutti i film
def query_tutti_film():
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM film ORDER BY titolo")
    risultato = cursor.fetchall()
    cursor.close()
    conn.close()
    return risultato
# Tutte le sale
def query_tutte_sale():
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sale")
    risultato = cursor.fetchall()
    cursor.close()
    conn.close()
    return risultato

def query_spettacolo(id_spettacolo):
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT spettacoli.*, film.titolo,
               sale.nome AS nome_sala, sale.posti
        FROM spettacoli
        JOIN film ON spettacoli.id_film = film.id_film
        JOIN sale ON spettacoli.id_sala = sale.id_sala
        WHERE spettacoli.id_spettacolo = %s
    """, (id_spettacolo,))
    risultato = cursor.fetchone()
    cursor.close()
    conn.close()
    return risultato

def query_biglietti_venduti(id_spettacolo):
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT COUNT(*) AS venduti FROM biglietti WHERE id_spettacolo = %s",
        (id_spettacolo,)
    )
    risultato = cursor.fetchone()
    cursor.close()
    conn.close()
    return risultato["venduti"]

def query_sale_con_numero_spettacoli():
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT sale.id_sala, sale.nome, sale.posti,
               COUNT(spettacoli.id_spettacolo) AS numero_spettacoli
        FROM sale
        LEFT JOIN spettacoli ON sale.id_sala = spettacoli.id_sala
        GROUP BY sale.id_sala, sale.nome, sale.posti
        ORDER BY sale.id_sala
    """)
    risultato = cursor.fetchall()
    cursor.close()
    conn.close()
    return risultato

def query_spettacoli_con_sala():
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT spettacoli.id_spettacolo, spettacoli.id_sala,
               spettacoli.data_ora, film.titolo,
               sale.nome AS nome_sala
        FROM spettacoli
        JOIN film ON spettacoli.id_film = film.id_film
        JOIN sale ON spettacoli.id_sala = sale.id_sala
        ORDER BY spettacoli.id_sala, spettacoli.data_ora
    """)
    risultato = cursor.fetchall()
    cursor.close()
    conn.close()
    return risultato

def inserisci_biglietto(id_spettacolo):
    conn = connetti()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO biglietti (id_spettacolo) VALUES (%s)",
        (id_spettacolo,)
    )
    conn.commit()
    cursor.close()
    conn.close()

def query_film(id_film):
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM film WHERE id_film = %s",
        (id_film,)
    )
    risultato = cursor.fetchone()
    cursor.close()
    conn.close()
    return risultato

def query_spettacoli_film(id_film):
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT spettacoli.*, sale.nome AS nome_sala
        FROM spettacoli
        JOIN sale ON spettacoli.id_sala = sale.id_sala
        WHERE spettacoli.id_film = %s
        ORDER BY spettacoli.data_ora
    """, (id_film,))
    risultato = cursor.fetchall()
    cursor.close()
    conn.close()
    return risultato

def query_totali():
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT COUNT(*) AS totale_biglietti,
               COALESCE(SUM(spettacoli.prezzo), 0) AS incasso_totale
        FROM biglietti
        JOIN spettacoli
          ON biglietti.id_spettacolo = spettacoli.id_spettacolo
    """)
    risultato = cursor.fetchone()
    cursor.close()
    conn.close()
    return risultato

def query_incasso_per_film():
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT film.id_film, film.titolo,
               COUNT(biglietti.id_biglietto) AS biglietti_venduti,
               COALESCE(
                   SUM(CASE WHEN biglietti.id_biglietto IS NOT NULL
                            THEN spettacoli.prezzo ELSE 0 END), 0
               ) AS incasso
        FROM film
        LEFT JOIN spettacoli ON film.id_film = spettacoli.id_film
        LEFT JOIN biglietti
          ON spettacoli.id_spettacolo = biglietti.id_spettacolo
        GROUP BY film.id_film, film.titolo
        ORDER BY biglietti_venduti DESC
    """)
    risultato = cursor.fetchall()
    cursor.close()
    conn.close()
    return risultato

def query_riempimento_spettacoli():
    conn = connetti()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT spettacoli.id_spettacolo,
               film.titolo,
               sale.nome AS nome_sala,
               sale.posti,
               COUNT(biglietti.id_biglietto) AS venduti,
               ROUND(COUNT(biglietti.id_biglietto) * 100 / sale.posti)
                   AS percentuale
        FROM spettacoli
        JOIN film ON spettacoli.id_film = film.id_film
        JOIN sale ON spettacoli.id_sala = sale.id_sala
        LEFT JOIN biglietti
          ON spettacoli.id_spettacolo = biglietti.id_spettacolo
        GROUP BY spettacoli.id_spettacolo,
                 film.titolo, sale.id_sala, sale.nome, sale.posti
        ORDER BY percentuale DESC
    """)
    risultato = cursor.fetchall()
    cursor.close()
    conn.close()
    return risultato

if __name__ == "__main__":
    print(query_riempimento_spettacoli())