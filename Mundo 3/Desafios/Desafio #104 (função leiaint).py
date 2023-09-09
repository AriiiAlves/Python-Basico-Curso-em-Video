def leiaint():
    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            n = int(n)
            #print(f'Você digitou o número {n}')
            return(n)
            break
        else:
            print('\033[1;31mErro: Digite um número válido!\033[m')


resp = leiaint()
print(f'Você digitou o número {resp}')