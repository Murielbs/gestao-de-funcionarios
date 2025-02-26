# cadastro_produtos.py
from utils import l

# Função de cadastro de produtos
def cadastrar_produto(codigo_barra):
    nome = input(f'Digite o nome do produto {codigo_barra}: ')
    preco = input(f'Digite o preço do produto {codigo_barra}: ')
    estoque = int(input(f'Digite a quantidade em estoque do produto {codigo_barra}: '))
    descricao = input(f'Digite a descrição do produto {codigo_barra}: ')
    return nome, preco, estoque, descricao

# Cadastro dos produtos
produto1, preco1, estoque1, descricao1 = cadastrar_produto(1234)
print(f'Código de barra: 1234')
l()
produto2, preco2, estoque2, descricao2 = cadastrar_produto(12345)
print(f'Código de barra: 12345')
l()

# Função de procura por código de barra
def procurar_produto():
    ID = input("Digite o código de barra do produto: ")
    l()
    if ID == '1234':
        print(f'O produto cadastrado com esse código é: {produto1}, temos {estoque1} no estoque')
    elif ID == '12345':
        print(f'O produto cadastrado com esse código é: {produto2}, temos {estoque2} no estoque')
    else:
        print("Código de barra não cadastrado")
        l()

# Função de atualização de produtos
def atualizar_produtos():
    atualiza = int(input("Digite o código de barra do produto que deseja atualizar:  "))

    if atualiza == 1234:
        print(f'O que você deseja atualizar do produto {produto1}?')
        resposta = input().lower()

        if resposta == 'preco':
            novo_preco = input("Digite o novo preço do produto: ")
            print(f'O produto {produto1} foi atualizado, novo preço: {novo_preco}')
        elif resposta == 'estoque':
            novo_estoque = input("Digite o novo estoque do produto: ")
            print(f'O produto {produto1} foi atualizado, novo estoque: {novo_estoque}')
        else:
            print("Opção inválida")
    elif atualiza == 12345:
        print(f'O que você deseja atualizar do produto {produto2}?')
        resposta = input().lower()
        if resposta == 'preco':
            novo_preco = input("Digite o novo preço do produto: ")
            print(f'O produto {produto2} foi atualizado, novo preço: {novo_preco}')
        elif resposta == 'estoque':
            novo_estoque = input("Digite o novo estoque do produto: ")
            print(f'O produto {produto2} foi atualizado, novo estoque: {novo_estoque}')
        else:
            print("Opção inválida")
    else:
        print("Código de barra não cadastrado")
        l()

# Apagar produto
def apagar_produtos():
    apagar = int(input("Digite o código de barra do produto que você deseja deletar: "))
    if apagar == 1234:
        print(f"O produto {produto1} foi apagado com sucesso.")
    elif apagar == 12345:
        print(f"O produto {produto2} foi apagado com sucesso.")
    else:
        print("Código de barra inválido.")
