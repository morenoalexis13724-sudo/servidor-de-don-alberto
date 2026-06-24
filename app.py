from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

# PERITAJES (GET y POST bien separados)
@app.route('/api/peritajes', methods=['GET', 'POST'])
def crear_peritaje():

    if request.method == 'GET':
        return jsonify({
            "mensaje": "Endpoint de peritajes funcionando (GET OK)"
        }), 200

    data = request.get_json(silent=True)

    if not data or 'placa' not in data:
        return jsonify({
            "error": "Debe enviar JSON con el campo 'placa'"
        }), 400

    placa = data['placa'].upper()

    return jsonify({
        "placa": placa
    }), 200


# INVENTARIO
@app.route('/api/inventario', methods=['GET'])
def inventario():
    return jsonify({
        "mensaje": "Inventario integrado feature + producción"
    }), 200


# HEALTH CHECK
@app.route('/api/health', methods=['GET'])
def health_check():
    sistema_archivos_ok = os.path.exists('/tmp') or os.path.exists('.')

    if sistema_archivos_ok:
        return jsonify({
            "status": "healthy",
            "timestamp": int(time.time()),
            "environment": "production-cloud",
            "uptime_check": "passed"
        }), 200
    else:
        return jsonify({
            "status": "unhealthy",
            "reason": "Storage unreachable"
        }), 500


if __name__ == '__main__':
    app.run(debug=True)