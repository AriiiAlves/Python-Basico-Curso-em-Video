def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return(False)
    else:
        return(True)

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        #write, text, + serve para criar caso não exista
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        return(a.readlines())
    finally:
        a.close()

def escreverArquivo(nome, lst):
    try:
        a = open(nome, 'at')
    except:
        print('Houve um erro ao editar o arquivo!')
    else:
        a.write(lst)
    finally:
        a.close()

def apagarArquivo(nome):
    try:
        a = open(nome, 'wt')
    except:
        print('Houve um erro ao apagar o arquivo!')
    finally:
        a.close()
