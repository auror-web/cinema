from flask import Flask, render_template, redirect, request
import database

app = Flask(__name__)

# ==========================================
# PAGINA 1 e 2: AURORA (index e Film)
# ==========================================

#index
@app.route("/")
def index():
    tf = database.query_tutti_film()
    return render_template("index.html", film=tf)


#film
@app.route("/film/<int:id_film>")
def film(id_film):
    f = database.query_film(id_film)
    s = database.query_spettacoli_film(id_film)
    return render_template("film.html", film=f, spettacoli=s)

# ==========================================
# PAGINA 3 & 4: CLAUDIA (Acquisto & Sale)
# ==========================================

#spettacolo
@app.route("/spettacolo/<int:id_spettacolo>")
def spettacolo(id_spettacolo):
    s = database.query_spettacolo(id_spettacolo)
    bv = database.query_biglietti_venduti(id_spettacolo)
    return render_template("spettacoli.html", spettacolo=s, bigliettI=bv)
#la query inserisci biglietto, non legge dal database ma inserisce una riga, quindi non dobbiamo assegnarlo ad una variabile come le altre perchè sarebbe vuota
@app.route("/spettacolo/<int:id_spettacolo>/acquista")
def acquista(id_spettacolo):
    s = database.query_spettacolo(id_spettacolo)
    bv = database.query_biglietti_venduti(id_spettacolo)

    #Se la sala ha ancora posti disponibili, inserisci il biglietto e ricarica
    if bv<s["posti"]:
        database.inserisci_biglietto(id_spettacolo)
    return redirect("/spettacolo/"+str(id_spettacolo))

#sale
@app.route("/sale")
def sale():
    sa= database.query_sale_con_numero_spettacoli()
    sp =database.query_spettacoli_con_sala()
    return render_template("sale.html", sale=sa, spettacoli=sp)


# ==========================================
# PAGINA 5: ROBERTO (Dashboard Incassi)
# ==========================================

#incassi
@app.route("/incassi")
def incassi():
    i=database.query_incasso_per_film()
    t=database.query_totali()
    r=database.query_riempimento_spettacoli()
    return render_template("incassi.html", incassi=i, totali=t, riempimento=r)


#main
if __name__ == "__main__":
    app.run(debug=True)