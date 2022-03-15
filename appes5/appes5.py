# Si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta.
# L'utente deve poter inserire il nome della squadra, la data di fondazione e la città.
# Deve inoltre poter effetuare delle ricerche inserendo uno dei valori delle colonne e ottenendo i dati presenti.

from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)