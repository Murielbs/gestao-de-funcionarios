# Função para imprimir uma linha de separação
def l():
    print("--" * 50)

# Função para cadastrar um funcionário
def cadastrar_funcionario(id_func):
    nome = input(f'Digite o nome do funcionário {id_func}: ')
    idade = int(input(f'Digite a idade do funcionário {id_func}: '))
    email = input(f'Digite o e-mail do funcionário {id_func}: ')
    telefone = input(f'Digite o telefone do funcionário {id_func}: ')
    return nome, idade, email, telefone

# Cadastro dos funcionários
nome1, idade1, email1, telefone1 = cadastrar_funcionario(1)
print("ID: 1")
l()
nome2, idade2, email2, telefone2 = cadastrar_funcionario(2)
print("ID: 2")

# Apresentar funcionários cadastrados
print(f'Funcionário {nome1} cadastrado')
l()
print(f'Funcionário {nome2} cadastrado')
l()

# Procurar funcionários pelo ID
ID = int(input('Digite o ID do funcionário: '))
l()
if ID == 1:
    print(f'O ID inserido pertence ao funcionário {nome1} // esse é o telefone para contato: {telefone1}')
    l()
elif ID == 2:
    print(f'O ID inserido pertence ao funcionário {nome2} // esse é o telefone para contato: {telefone2}')
    l()
else:
    print('Funcionário não encontrado')
    l()

# Atualizar dados do funcionário
def atualizar_dados():
    atualizar = int(input("Digite o ID do funcionário para atualizar algum dado: "))
    if atualizar == 1:
        print(f'O que você deseja atualizar do funcionário {nome1}?')
        resposta = input().lower()
        if resposta == "idade":
            nova_idade = int(input("Adicione a nova idade: "))
            print(f'Dados do funcionário atualizados, nova idade: {nova_idade}')
        elif resposta == "email":
            novo_email = input("Adicione o novo email: ")
            print(f'Dados do funcionário atualizados, novo email: {novo_email}')
        elif resposta == "telefone":
            novo_telefone = input("Adicione o novo telefone: ")
            print(f'Dados do funcionário atualizados, novo telefone: {novo_telefone}')
        else:
            print("Opção inválida.")
    elif atualizar == 2:
        print(f'O que você deseja atualizar do funcionário {nome2}?')
        resposta = input().lower()
        if resposta == "idade":
            nova_idade = int(input("Adicione a nova idade: "))
            print(f'Dados do funcionário atualizados, nova idade: {nova_idade}')
        elif resposta == "email":
            novo_email = input("Adicione o novo email: ")
            print(f'Dados do funcionário atualizados, novo email: {novo_email}')
        elif resposta == "telefone":
            novo_telefone = input("Adicione o novo telefone: ")
            print(f'Dados do funcionário atualizados, novo telefone: {novo_telefone}')
        else:
            print("Opção inválida.")
    else:
        print("ID inválido.")

atualizar_dados()

# Apagar funcionário
def apagar_funcionario():
    apagar = int(input("Digite o ID do funcionário que você quer apagar: "))
    if apagar == 1:
        print(f"O funcionário {nome1} foi apagado com sucesso.")
    elif apagar == 2:
        print(f"O funcionário {nome2} foi apagado com sucesso.")
    else:
        print("ID inválido.")

apagar_funcionario()
