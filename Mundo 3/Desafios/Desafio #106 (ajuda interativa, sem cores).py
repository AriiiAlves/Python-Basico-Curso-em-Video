def line():
    print('-' * 50)


'''def title():
    line()
    print('SISTEMA DE AJUDA HELP'.center(50))
    line()

def fhelp(x):
    help()'''


def fhelp():
    line()
    print('SISTEMA DE AJUDA HELP'.center(50))
    line()
    while True:
        x = input(('Digite a Função ou biblioteca: '))
        if x.strip().upper() == 'FIM':
            break
        elif x == '':
            print('\033[0;31mNenhum valor digitado!\033[m')
        else:
            line()
            print(f'ACESSANDO MANUAL DO COMANDO {x}'.center(50))
            line()
            help(x)
            line()


fhelp()