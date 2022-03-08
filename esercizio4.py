#4. modificare il server precedente per far sì che quando l'utente clicca sulla terza immagine venga visualizzato il numero di giorni che mancano alla fine della scuola. 
# Utilizzare un file css per definire la grafica della pagina. La route per accedere al serizio deve essere /quantomanca
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('indexcss.html')

@app.route('/quantomanca', methods=['GET'])
def finescuola():


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)