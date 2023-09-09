from os import remove

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return(False)
    else:
        return(True)

def criarArquivo(arq, new=False):
    try:
        a = open(arq, 'wt+')
        #write, text, + serve para criar caso não exista
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        if new:
            print('-'*40)
            print(f'Arquivo {arq} limpo com sucesso')
        else:
            print(f'Arquivo {arq} criado com sucesso')

def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(a.read())
    finally:
        a.close()

# def contarTexto():
#     try:
#         a = open(arq, )

def escreverArquivo(arq, n, i):
    try:
        a = open(arq, 'rt')
        b = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        if a.read() in '':
            try:
                b.write(f'{n:<30}{i:^10}')
            except Exception as erro:
                print(f'Erro ao editar: {erro}')
        else:
            try:
                b.write(f'\n{n:<30}{i:^10}')
            except Exception as erro:
                print(f'Erro ao editar: {erro}')
    finally:
        a.close()

def apagarArquivo(arq):
    remove(arq)
