from flask import Flask, request

app = Flask(__name__)

# PRODUCCIÓN (BUG DEL TALLER)
@app.route('/api/peritajes', methods=['POST'])
def crear_peritaje():
    data = request.json
    placa = data['placa'].upper()   # <-- ESTE ES EL BUG
    return {"placa": placa}


# FEATURE INVENTARIO
@app.route('/api/inventario', methods=['GET'])
def inventario():
    return {"mensaje": "Inventario en produccion estable"}


if __name__ == '__main__':
    app.run(debug=True)
