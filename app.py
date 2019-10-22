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
    medicion_list = requests.get('https://api-evergreen-luis.azurewebsites.net/Mediciones').json()
    return render_template('listaMedicion.html', mediciones=medicion_list)

@app.route("/guardarMedicion", methods=['POST'])
def guardarMedicion():
    medicion = dict(request.values)
    medicion['valor'] = int(medicion['valor'])
    requests.post('https://api-evergreen-luis.azurewebsites.net/Mediciones',json=medicion)
    return(listarMediciones())

@app.route("/")
def hello():
    return "Hello World!"
