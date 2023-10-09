import requests

url = 'http://localhost:5000/dados'  # Substitua pela URL correta da sua API

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Dados recebidos da API:")
        print(data)
    else:
        print(f'Erro: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Erro na solicitação: {e}')
