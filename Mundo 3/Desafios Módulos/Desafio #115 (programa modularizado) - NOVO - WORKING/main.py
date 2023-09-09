import cadastro
import arquivo
from time import sleep

arq = '#115 Lista de Cadastrados.txt'

if arquivo.arquivoExiste(arq):
    print('Backup de cadastro encontrado com sucesso!')
    print('Inicializando sistema...')
    sleep(1)
else:
    print('Backup de cadastro não encontrado!')
    arquivo.criarArquivo('#115 Lista de Cadastrados.txt')
    print('Backup de cadastro criado com sucesso!')
    print('Inicializando sistema...')
    sleep(1)

cadastro.menu(arq)