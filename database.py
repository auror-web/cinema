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

if __name__ == "__main__":
    print(query_sale_con_numero_spettacoli())

