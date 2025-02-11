from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Path to clients directory
CLIENTS_DIR = os.path.join(os.getcwd(), 'clients')

@app.route('/')
def index():
    clients = [
        {'name': 'Resent Client', 'path': 'ResentClient'},
        {'name': 'Astra Client', 'path': 'AstraClient'},
        {'name': 'Eagler 1.8.8', 'path': 'Eagler188'},
        {'name': 'Eagler 1.5.2', 'path': 'Eagler152'},
        {'name': 'EaglerMobile', 'path': 'EaglerMobile'}
    ]
    return render_template('index.html', clients=clients)

@app.route('/launch/<client_name>')
def launch_client(client_name):
    client_path = os.path.join(CLIENTS_DIR, client_name, 'index.html')
    if os.path.exists(client_path):
        return send_from_directory(os.path.join(CLIENTS_DIR, client_name), 'index.html')
    else:
        return "Client not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
