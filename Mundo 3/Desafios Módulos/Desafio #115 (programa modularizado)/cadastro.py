from arquivo import escreverArquivo, apagarArquivo

arq=0
lista_cadastrados = []

def cor(num=3):
    cores =  ('\033[0;33m', # 0 = Amarelo
              '\033[0;34m', # 1 = Azul
              '\033[0;32m', # 2 = Verde
              '\033[0;31m', # 3 = Vermelho
              '\033[m', # 4 = Reset
              )
    return(cores[num])

def novo_cadastro():
    dados = {}
    print('-' * 40)
    print('NOVO CADASTRO'.center(40))
    print('-' * 40)
    nome = str(input('Digite o Nome: ')).lower().strip().title()
    idade = int(input('Digite a idade: '))
    dados['nome'] = nome
    dados['idade'] = idade
    return(dados.copy())

def cadastrados(show=False, new=0):
    global lista_cadastrados
    if new != 0:
        lista_cadastrados.append(new)
    if show == True:
        print('-' * 40)
        print('CADASTRADOS'.center(40))
        print('-' * 40)
        for pessoa in lista_cadastrados:
            print(f'{pessoa["nome"]:<30}'
                  f'{pessoa["idade"]:} Anos'.center(10))

def menu(arq):
    while True:
        try:
            print('-'*40)
            print('MENU PRINCIPAL'.center(40))
            print('-' * 40)
            print(f'{cor(0)}1{cor(4)} - {cor(1)}Ver pessoas cadastradas{cor(4)}'
                  f'\n{cor(0)}2{cor(4)} - {cor(1)}Cadastrar nova pessoa{cor(4)}'
                  f'\n{cor(0)}3{cor(4)} - {cor(1)}Sair do sistema{cor(4)}')
            print('-' * 40)
            escolha = int(input('Sua opção: '))
            if escolha == 1:
                cadastrados(True)
            elif escolha == 2:
                dados = novo_cadastro()
                cadastrados(False, dados)
            elif escolha == 3:
                break
            else:
                print(f'{cor(3)}ERRO DE OPÇÃO{cor(4)}')
            apagarArquivo(arq)
            lista = str(lista_cadastrados)
            escreverArquivo(arq, lista)
        except Exception as erro:
            print(f'{cor(3)}Erro: {erro}{cor(4)}')