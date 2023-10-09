import os
from flask import Flask, jsonify

app = Flask(__name__)

# Obtém o diretório atual do arquivo Python
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, 'data.json')

# Rota para fornecer os dados do JSON
@app.route('/dados', methods=['GET'])
def obter_dados():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json_file.read()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
