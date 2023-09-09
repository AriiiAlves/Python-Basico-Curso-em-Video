from arquivo import escreverArquivo, lerArquivo, apagarArquivo, criarArquivo

arq=0
dados = {}

def cor(num=3):
    cores =  ('\033[0;33m', # 0 = Amarelo
              '\033[0;34m', # 1 = Azul
              '\033[0;32m', # 2 = Verde
              '\033[0;31m', # 3 = Vermelho
              '\033[m', # 4 = Reset
              )
    return(cores[num])

def novo_cadastro(arq):
    print('-' * 40)
    print('NOVO CADASTRO'.center(40))
    print('-' * 40)
    nome = str(input('Digite o Nome: ')).lower().strip().title()
    idade = int(input('Digite a idade: '))
    idade = str(f'{idade} Anos')
    escreverArquivo(arq, nome, idade)

def cadastrados(arq, show=False):
    if show == True:
        print('-' * 40)
        print('CADASTRADOS'.center(40))
        print('-' * 40)
        lerArquivo(arq)

def menu(arq):
    while True:
        try:
            print('-'*40)
            print('MENU PRINCIPAL'.center(40))
            print('-' * 40)
            print(f'{cor(0)}1{cor(4)} - {cor(1)}Ver pessoas cadastradas{cor(4)}'
                  f'\n{cor(0)}2{cor(4)} - {cor(1)}Cadastrar nova pessoa{cor(4)}'
                  f'\n{cor(0)}3{cor(4)} - {cor(1)}Sair do sistema{cor(4)}'
                  f'\n{cor(0)}99{cor(4)} - {cor(1)}Limpar cadastrados{cor(4)}')
            print('-' * 40)
            escolha = int(input(f'{cor(2)}Sua opção: {cor(4)}'))
            if escolha == 1:
                cadastrados(arq, True)
            elif escolha == 2:
                novo_cadastro(arq)
            elif escolha == 3:
                break
            elif escolha == 99:
                apagarArquivo(arq)
                criarArquivo('#115 Lista de Cadastrados.txt', True)
            else:
                print(f'{cor(3)}ERRO DE OPÇÃO{cor(4)}')
        except Exception as erro:
            print(f'{cor(3)}Erro: {erro}{cor(4)}')