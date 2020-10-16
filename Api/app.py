from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/mensaje', methods=['GET'])
def ObtenerMensaje():
    return jsonify( {'mensaje': 'Este es un mensaje :D!! '} )

# PARA CORRER EL ARCHIVO EN LA CONSOLA ES python app.py
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)