import os

def criar_novo_codigo():
    linguagem = input("Digite a linguagem de programação: ")
    nome_arquivo = input("Digite o nome do arquivo: ")
    nome_arquivo += f".{linguagem}"

    # Verifica se o arquivo já existe
    if os.path.exists(nome_arquivo):
        print("Este arquivo já existe.")
        return

    # Cria o arquivo com o comando nano
    os.system(f"nano {nome_arquivo}")
    print("Arquivo criado com sucesso!")

def abrir_codigo_salvo():
    nome_arquivo = input("Digite o nome do arquivo a ser aberto: ")

    # Verifica se o arquivo existe
    if not os.path.exists(nome_arquivo):
        print("Este arquivo não existe.")
        return

    # Abre o arquivo com o comando nano
    os.system(f"nano {nome_arquivo}")

def menu():
    print("1. Criar novo código")
    print("2. Abrir código salvo")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_novo_codigo()
    elif opcao == "2":
        abrir_codigo_salvo()
    elif opcao == "3":
        exit()
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        menu()

while True:
    menu()
