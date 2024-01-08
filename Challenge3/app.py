from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)
mongo_host = os.environ.get('MONGO_HOST', 'mongodb')
mongo_port = int(os.environ.get('MONGO_PORT', 27017))
database_name = os.environ.get('DATABASE_NAME', 'your_database')

client = MongoClient(host=mongo_host, port=mongo_port)
db = client[database_name]

@app.route("/")
def hello_world():
    # Récupérez les 10 derniers enregistrements depuis la base de données
    records = list(db.records.find().sort('_id', -1).limit(10))

    # Préparez les données pour l'affichage
    display_data = [{'ip_address': record['ip_address'], 'timestamp': record['timestamp']} for record in records]

    # Passez les données au modèle Flask pour l'affichage
    return render_template('index.html', records=display_data)

# Cette route sera appelée à chaque requête et enregistrera l'adresse IP et l'heure
@app.before_request
def before_request():
    client_ip = request.remote_addr
    current_date = datetime.now()

    # Enregistrez les informations dans la base de données MongoDB
    db.records.insert_one({
        'ip_address': client_ip,
        'timestamp': current_date
    })

# Cette route est optionnelle, elle permet d'afficher un message de confirmation
@app.route("/save_record")
def save_record():
    return "Record saved successfully"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
