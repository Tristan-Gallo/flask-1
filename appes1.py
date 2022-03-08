# Realizzare un server web che permetta di effetuare il login
# L'utente inserisce lo username e la password:
# se lo username è admin e la password è xxx123##, il sito ci saluta con un messaggio di benvenuto
# altrimenti ci da un messaggio di errore.
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('form2.html')

@app.route('/data', methods=['GET'])
def data():
  password = request.args['Password']
  username = request.args['Name']
  if username == 'admin' and password == 'xxx123##':
    return render_template('welcome.html')
  else:
      return '<h1>Errore</h1>'  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)