from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

# PRODUCCIÓN (BUG DEL TALLER)
@app.route('/api/peritajes', methods=['POST'])
def crear_peritaje():
    data = request.json
    placa = data['placa'].upper()
    return {"placa": placa}


# FEATURE INVENTARIO
@app.route('/api/inventario', methods=['GET'])
def inventario():
    return {"mensaje": "Inventario integrado feature + producción"}


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