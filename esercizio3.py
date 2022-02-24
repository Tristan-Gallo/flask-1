#3. modificare il server precedente per far sì chhe quando l'utente clicca sulla seconda immagine il server web risponde con una frase celebre, scelta casualmente da un elenco 
# di 10 frasi (per ispirazione  https://www.frasimania.it/frasi-corte/). Utilizzare una struttura dati adatta per contenere le frasi e gli autori Il sito deve visualizzare la 
# frase con una certa grafica (a scelta) e anche l'autore (da visualizzare con una grafica diversa). Utilizzare un file css per definire la grafica della pagina.La route per 
# accedere al serizio deve essere /frasicelebri
from flask import Flask, render_template
app = Flask(__name__)

import random

@app.route('/', methods=['GET'])
def home():
    return render_template('indexcss.html')

@app.route('/frasicelebri', methods=['GET'])
def frasi():
    



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)