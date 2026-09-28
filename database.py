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

if __name__ == "__main__":
  print(query_tutti_film())