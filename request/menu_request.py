import requests

def listar_pessoas():
    url = 'http://localhost:5000/dados'  #URL de requisição a api

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("Dados recebidos da API:")
            for pessoa in data:
                print("---------")
                print(f"ID: {pessoa['id']}")
                print(f"NOME: {pessoa['nome']}")
                print(f"IDADE: {pessoa['idade']}")
                print(f"CIDADE: {pessoa['cidade']}")
                print(f"UF: {pessoa['uf']}")
        else:
            print(f'Erro: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')

def buscar_pessoas_por_idade():
    idade = int(input("Digite a idade que deseja buscar: "))
    url = f'http://localhost:5000/pessoas/idade/{idade}'  

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if not data:
                print(f"Nenhuma pessoa encontrada com a idade {idade}.")
            else:
                print(f"Pessoas encontradas com a idade {idade}:")
                for pessoa in data:
                    print("---------")
                    print(f"ID: {pessoa['id']}")
                    print(f"NOME: {pessoa['nome']}")
                    print(f"IDADE: {pessoa['idade']}")
                    print(f"CIDADE: {pessoa['cidade']}")
                    print(f"UF: {pessoa['uf']}")
        else:
            print(f'Erro: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')

def cadastrar_pessoa():
    # Solicita os dados da nova pessoa ao usuário
    nome = input("Digite o nome da nova pessoa: ")
    idade = int(input("Digite a idade da nova pessoa: "))
    cidade = input("Digite a cidade da nova pessoa: ")
    uf = input("Digite a UF da nova pessoa: ")

    # Cria um dicionário com os dados da nova pessoa
    nova_pessoa = {
        "id": None,  # Define o ID como None temporariamente
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "uf": uf
    }

    url = 'http://localhost:5000/pessoas'  

    try:
        response = requests.post(url, json=nova_pessoa)

        if response.status_code == 201:
            nova_pessoa = response.json()
            print("Nova pessoa cadastrada com sucesso!")
            print(f"ID da nova pessoa: {nova_pessoa['id']}")
        else:
            print(f'Erro: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')

def excluir_pessoa():
    usuario_id = int(input("Digite o ID da pessoa que deseja excluir: "))
    url = f'http://localhost:5000/pessoas/excluir/{usuario_id}'  

    try:
        response = requests.delete(url)

        if response.status_code == 200:
            print(f"Pessoa com ID {usuario_id} excluída com sucesso!")
        elif response.status_code == 404:
            print(f"Nenhuma pessoa encontrada com o ID {usuario_id}.")
        else:
            print(f'Erro: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')

def main():
    while True:
        print("\nO que você gostaria de fazer?")
        print("1 - Listar Pessoas")
        print("2 - Cadastrar Pessoa")
        print("3 - Excluir Pessoa")
        print("4 - Procurar Pessoas com Idade X")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            # Opção de Listar Pessoas
            listar_pessoas()
        elif escolha == '2':
            # Opção de Cadastrar Pessoa
            cadastrar_pessoa()
        elif escolha == '3':
            # Opção de Excluir Pessoa
            excluir_pessoa()
        elif escolha == '4':
            # Opção de Procurar Pessoas com Idade X
            buscar_pessoas_por_idade()
        elif escolha == '0':
            # Opção de Sair
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    main()
