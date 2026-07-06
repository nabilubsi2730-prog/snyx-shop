import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Mengizinkan Frontend Node.js mengakses API ini

# Data Guitar Dummy (Bisa disesuaikan dengan milikmu)
guitars = [
    {"id": "1", "name": "Yamaha F310", "category": "Akustik", "price": "1.500.000", "description": "Gitar akustik cocok untuk pemula dengan suara jernih.", "popular": True},
    {"id": "2", "name": "Cort", "category": "Klasik", "price": "2.000.000", "description": "Gitar klasik dengan senar nylon cocok untuk festival.", "popular": True},
    {"id": "3", "name": "Taylor GS Mini", "category": "Akustik", "price": "9.000.000", "description": "Gitar akustik premium dengan suara berkelas.", "popular": False},
    {"id": "4", "name": "Cordoba C5", "category": "Klasik", "price": "3.000.000", "description": "Gitar klasik dengan senar nylon cocok untuk latihan.", "popular": False},
    {"id": "5", "name": "Ibanez RG350", "category": "Listrik", "price": "7.000.000", "description": "Gitar listrik cocok untuk musik metal dan shredder.", "popular": False},
    {"id": "6", "name": "Fender Stratocaster", "category": "Listrik", "price": "15.000.000", "description": "Gitar listrik dengan suara jernih cocok untuk blues.", "popular": False}
]

@app.route('/api/guitars', methods=['GET'])
def get_guitars():
    return jsonify(guitars)

@app.route('/api/guitars/<id>', methods=['GET'])
def get_guitar_by_id(id):
    guitar = next((g for g in guitars if g['id'] == id), None)
    if guitar:
        return jsonify(guitar)
    return jsonify({"message": "Gitar tidak ditemukan"}), 404

@app.route('/api/guitars', methods=['POST'])
def add_guitar():
    data = request.json
    new_id = str(len(guitars) + 1)
    new_guitar = {
        "id": new_id,
        "name": data.get('name'),
        "category": data.get('category'),
        "price": data.get('price'),
        "description": data.get('description'),
        "popular": data.get('popular', False)
    }
    guitars.append(new_guitar)
    return jsonify(new_guitar), 201

@app.route('/api/guitars/<id>', methods=['PUT'])
def update_guitar(id):
    data = request.json
    guitar = next((g for g in guitars if g['id'] == id), None)
    if guitar:
        guitar.update({
            "name": data.get('name', guitar['name']),
            "category": data.get('category', guitar['category']),
            "price": data.get('price', guitar['price']),
            "description": data.get('description', guitar['description']),
            "popular": data.get('popular', guitar['popular'])
        })
        return jsonify(guitar)
    return jsonify({"message": "Gitar tidak ditemukan"}), 404

@app.route('/api/guitars/<id>', methods=['DELETE'])
def delete_guitar(id):
    global guitars
    guitars = [g for g in guitars if g['id'] != id]
    return jsonify({"message": "Gitar berhasil dihapus"}), 200

# LANGKAH CRITICAL: Menggunakan Port dinamis dari Cloud Environment
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)