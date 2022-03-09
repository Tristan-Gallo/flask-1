# Realizzare un server web che permetta di conoscere capoluoghi di regione.
# L'utente inserisce il nome della regione e il programma restituisce il nome del capoluogo della regione.
# Caricare i capoluoghi di regione e le regioni in una opportuna struttura dati.

# Modificare poi l'esercizio precedente per permettere all'utente di inserire un capoluogo e di avere la regione in cui si trova.
# L'utente sceglie se avere la regione o il capoluogo selezionando un radio button.

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('formappes3.html')

@app.route('/scelta', methods=['GET'])
def scelta():
    scelta = request.args['Scelta']

@app.route('/regione', methods=['GET'])
def regioni():
    capoluoghiRegione = {'Abruzzo':'L\'Aquila', 'Basilicata':'Potenza', 'Calabria':'Catanzaro', 'Campania':'Napoli', 'Emilia-Romagna':'Bologna', 'Friuli-Venezia Giulia':'Trieste', 'Lazio':'Roma', 'Liguria':'Genova', 'Lombardia':'Milano', 'Marche':'Ancona', 'Molise':'Campobasso', 'Piemonte':'Torino', 'Puglia':'Bari', 'Sardegna':'Cagliari', 'Sicilia':'Palermo', 'Toscana':'Firenze', 'Trentino-Alto Adige':'Trento', 'Umbria':'Perugia', 'Valle dAosta':'Aosta', 'Veneto':'Venezia'}
    items = list(capoluoghiRegione.items())
    reg = request.args['Regione']
    for item in items:
        if item[0]==reg:
            r = item[1]
        else:
            return render_template('errore-es3.html')
    return r

@app.route('/capoluoghi', methods=['GET'])
def capoluoghi():


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)