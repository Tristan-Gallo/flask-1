# Si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta.
# L'utente deve poter inserire il nome della squadra, la data di fondazione e la città.
# Deve inoltre poter effetuare delle ricerche inserendo uno dei valori delle colonne e ottenendo i dati presenti.

from flask import Flask, render_template, request 
import pandas as pd 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("scegli.html")

@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template('inserisci.html')

@app.route('/ricerca', methods=['GET'])
def ricerca():
    return render_template('ricerca.html')

@app.route("/inseriscidati", methods=["GET"])
def inseriscidati():
    squadra = request.args["Squadra"]
    anno = request.args["Anno"]
    citta = request.args["Citta"]
    df = pd.read_csv("/workspace/flask/templates/datisquadre.csv")
    dUtente = {"Squadra" : squadra, "Anno" : anno, "Città" : citta}
    df = df.append(dUtente, ignore_index = True)
    df.to_csv("/workspace/flask/templates/datisquadre.csv", index=False)
    return render_template('scegli.html')

@app.route('/ricercadati', methods=['GET'])
def ricercadati():
    scelta = request.args['Scelta']
    ricerca = request.args['Ricerca']
    df = pd.read_csv('/workspace/flask/templates/datisquadre.csv')
    if scelta == 'Squadra':
        info = df[df['Squadra'] == ricerca]
    elif scelta == 'Anno':
        info = df[df['Anno'] == ricerca]
    else:
        info = df[df['Citta'] == ricerca]
    return info.to_html()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)