from flask import Flask, jsonify, render_template, request
import requests


app = Flask(__name__, template_folder='templates')

origenes_list = [
    'Sensor en terreno', 
    'Imagen satelital', 
    'Imagen dron', 
    'Dato derivado'
]

@app.route('/crearMedicion', methods=['GET'])
def crearmedicion():
    return render_template('crearMedicion.html', origenes=origenes_list)

@app.route("/listarMediciones", methods=['GET'])
def listarMediciones():
    medicion_list = requests.get('http://localhost:4000/Mediciones').json()
    return render_template('listaMedicion.html', mediciones=medicion_list)

@app.route("/guardarMedicion", methods=['POST'])
def guardarMedicion():
    medicion = dict(request.values)
    medicion['valor'] = int(medicion['valor'])
    requests.post('http://localhost:4000/Mediciones',json=medicion)
    return(listarMediciones())

app.run(port=8000, debug=True)
