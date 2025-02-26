# cadastro_clientes.py
from utils import l

# Função de cadastro de clientes
def cadastrar_cliente(id_cliente):
    nome = input(f'Digite o nome do cliente {id_cliente}: ')
    email = input(f'Digite o e-mail do cliente {id_cliente}: ')
    telefone = input(f'Digite o telefone do cliente {id_cliente}: ')
    return nome, email, telefone

# Cadastro dos clientes
cliente1, email_cliente1, telefone_cliente1 = cadastrar_cliente(1)
print("ID: 1")
l()
cliente2, email_cliente2, telefone_cliente2 = cadastrar_cliente(2)
print("ID: 2")
l()

# Apresentar clientes cadastrados
print(f'Cliente {cliente1} cadastrado')
l()
print(f'Cliente {cliente2} cadastrado')
l()

# Função de procura de cliente
def procurar_cliente():
    id_cliente = int(input('Digite o ID do cliente: '))
    l()
    if id_cliente == 1:
        print(f'O ID inserido pertence ao cliente {cliente1} // Esse é o telefone para contato: {telefone_cliente1}')
        l()
    elif id_cliente == 2:
        print(f'O ID inserido pertence ao cliente {cliente2} // Esse é o telefone para contato: {telefone_cliente2}')
        l()
    else:
        print('Cliente não encontrado')
        l()

# Atualizar dados do cliente
def atualizar_cliente():
    Atualizar = int(input("Digite o ID do cliente para atualizar algum dado:  "))

    if Atualizar == 1:
        print(f'O que você deseja atualizar do cliente {cliente1}?')
        resposta = input()

        if resposta.lower() == "email":
            novo_email = input("Adicione o novo email: ")
            print(f"Dados do cliente atualizados, novo email: {novo_email}")
        elif resposta.lower() == "telefone":
            novo_telefone = input("Adicione o novo telefone: ")
            print(f"Dados do cliente atualizados, novo telefone: {novo_telefone}")
        else:
            print("Opção inválida.")
    elif Atualizar == 2:
        print(f'O que você deseja atualizar do cliente {cliente2}?')
        resposta = input()

        if resposta.lower() == "email":
            novo_email = input("Adicione o novo email: ")
            print(f"Dados do cliente atualizados, novo email: {novo_email}")
        elif resposta.lower() == "telefone":
            novo_telefone = input("Adicione o novo telefone: ")
            print(f"Dados do cliente atualizados, novo telefone: {novo_telefone}")
        else:
            print("Opção inválida.")
    else:
        print("ID inválido.")
        l()

# Apagar cliente
def apagar_cliente():
    apagar = int(input("Digite o ID do cliente que você quer apagar: "))
    if apagar == 1:
        print(f"O cliente {cliente1} foi apagado com sucesso.")
    elif apagar == 2:
        print(f"O cliente {cliente2} foi apagado com sucesso.")
    else:
        print("ID inválido.")
