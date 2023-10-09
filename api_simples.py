import os
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Obtém o diretório atual do arquivo Python
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, 'data.json')

# Carrega os dados do arquivo JSON em uma lista de dicionários
def carregar_dados():
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

# Rota para fornecer os dados do JSON
@app.route('/dados', methods=['GET'])
def obter_dados():
    data = carregar_dados()
    return jsonify(data)

# Rota para buscar pessoas por idade
@app.route('/pessoas/idade/<int:idade>', methods=['GET'])
def buscar_pessoas_por_idade(idade):
    data = carregar_dados()
    pessoas_com_idade = [pessoa for pessoa in data if pessoa['idade'] == idade]
    return jsonify(pessoas_com_idade)

# Rota para cadastrar um novo usuário
@app.route('/pessoas', methods=['POST'])
def cadastrar_pessoa():
    data = carregar_dados()

    # Encontra o maior ID existente
    max_id = max([pessoa["id"] for pessoa in data])

    # Obtém os dados enviados no corpo da solicitação POST
    novo_usuario = request.json
    novo_usuario["id"] = max_id + 1

    data.append(novo_usuario)

    # Atualiza o arquivo JSON com o novo usuário
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    return jsonify(novo_usuario), 201

# Rota para excluir um usuário por ID
@app.route('/pessoas/excluir/<int:usuario_id>', methods=['DELETE'])
def excluir_pessoa(usuario_id):
    data = carregar_dados()

    # Encontra e remove o usuário com o ID especificado
    usuario_removido = None
    for usuario in data:
        if usuario['id'] == usuario_id:
            usuario_removido = usuario
            data.remove(usuario)
            break

    if usuario_removido:
        # Atualiza o arquivo JSON após a remoção do usuário
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return jsonify({"message": f"Usuário com ID {usuario_id} excluído."}), 200
    else:
        return jsonify({"message": f"Nenhum usuário encontrado com o ID {usuario_id}."}), 404

if __name__ == '__main__':
    app.run(debug=True)
