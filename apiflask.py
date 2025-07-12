from flask import Flask, request, jsonify
from flask_cors import CORS  # ⬅ ajouter ça
from app_agi import lancer_appel  # ton script AMI

app = Flask(_name_)
CORS(app)

@app.route('/call', methods=['POST'])
def call():
    data = request.json
    depuis = data.get('from')
    vers = data.get('to')

    if not depuis or not vers:
        return jsonify({'error': 'Paramètres manquants'}), 400

    try:
        lancer_appel(depuis, vers)
        return jsonify({'status': 'appel lancé'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if _name_ == '_main_':
    app.run(port=5000)
