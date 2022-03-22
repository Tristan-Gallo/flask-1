# Realizzare un sito web che restituisca la mappa dei quartieri di Milano.
# Ci deve essere una home page con un link quartieri di Milano: cliccando su questo link si deve visualizzare la mappa dei quartieri di Milano.

from flask import Flask, render_template, send_file, make_response, url_for, Response
app = Flask(__name__)

import geopandas as gpd 
import contextily as ctx
import matplotlib.pyplot as plt 

quartieri = gpd.read_file('/workspace/flask/NIL_WM.dbf')

@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')

@app.route('/quartieri', methods=['GET'])
def quartieri():
    fig, ax = plt.subplots(figsize = (12,8))
    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    ctx.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)