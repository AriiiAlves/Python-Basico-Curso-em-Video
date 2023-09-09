import cadastro
import arquivo
from time import sleep

arq = '#115 Lista de Cadastrados.txt'
listalst = 'oi'
lista_cadastrados = []

if arquivo.arquivoExiste(arq):
    print('Backup de cadastro encontrado com sucesso!')
    print('Inicializando sistema...')
    sleep(1)
else:
    print('Backup de cadastro não encontrado!')
    arquivo.criarArquivo('#115 Lista de Cadastrados.txt')
    arquivo.escreverArquivo(arq, f'{lista_cadastrados}')
    print('Backup de cadastro criado com sucesso!')
    print('Inicializando sistema...')
    sleep(1)

listalst = list(arquivo.lerArquivo(arq))
lista_cadastrados = listalst
print(lista_cadastrados)
cadastro.menu(arq)