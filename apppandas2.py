from flask import Flask, request, render_template, send_file, make_response, url_for, Response
app = Flask(__name__)

import io
import geopandas as gpd
import contextily as ctx
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

quartieri = gpd.read_file('/workspace/flask/ds964_nil_wm (1).zip')
fontanelle = gpd.read_file('/workspace/flask/Fontanelle.zip')

@app.route('/', methods=['GET'])
def home():
    return render_template('homepage2.html')

@app.route('/visualizza', methods=['GET'])
def visualizzaRis():
    fig, ax = plt.subplots(figsize = (12,8))

    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    ctx.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/ricercapng", methods=["GET"])
def ricercaRis():
    fig, ax = plt.subplots(figsize = (12,8))

    imgUtente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    ctx.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/ricerca', methods=['GET'])
def ricerca():
    return render_template('ricercaquartiere.html')

@app.route('/ricercaris', methods=("POST", "GET"))
def Ricerca():
    global imgUtente
    quartiereUtente = request.args["Quartiere"]
    imgUtente = quartieri[quartieri["NIL"] == quartiereUtente]
    if len(imgUtente) == 0:
        return "<h1>Il quartiere inserito non esiste</h1>"
    else:
        return render_template('ricercaris.html', PageTitle = "Matplotlib", quartiere=quartiereUtente)

@app.route('/scelta', methods=('POST', 'GET'))
def scelta():
    return render_template('sceltaquartiere.html', quartieri= quartieri["NIL"])

@app.route("/fontanelle", methods=["GET"])
def fontanelle1():
    return render_template("fontanelle.html", quartieri= quartieri["NIL"])

@app.route('/fontanelleris', methods=("POST", "GET"))
def fontanelleRis():
    global imgUtente, fontQuart
    quartiereUtente = request.args["Quartiere"]
    imgUtente = quartieri[quartieri["NIL"] == quartiereUtente]
    fontQuart = fontanelle[fontanelle.within(imgUtente.geometry.squeeze())]
    print(fontQuart)
    return render_template('fontanelleris.html', PageTitle = "Matplotlib", quartiere=quartiereUtente, tabella = fontQuart.to_html())

@app.route('/fontanellepng', methods=['GET'])
def Fontanelle():
    fig, ax = plt.subplots(figsize = (12,8))

    imgUtente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    fontQuart.to_crs(epsg=3857).plot(ax=ax, color="r")
    ctx.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)