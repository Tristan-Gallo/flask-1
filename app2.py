#realizzare un server web che visualizzi l'ora e colori lo sfondo in base all'orario: un colore per la mattina, uno per il pomeriggio, uno per la sera e uno per la notte
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

time = datetime.today().strftime('%H:%M')

@app.route('/', methods=['GET'])
def orario():
    return time

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

