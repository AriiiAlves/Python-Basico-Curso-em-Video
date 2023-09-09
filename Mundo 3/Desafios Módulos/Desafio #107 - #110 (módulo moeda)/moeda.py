def moeda(num):
    return(f'R$ {num}')

def aumentar(num, por, form=False):
    x = num + (num * (por / 100))
    if form == True:
        return(moeda(x))
    else:
        return (x)


def diminuir(num, por, form=False):
    x = num - (num * (por / 100))
    if form == True:
        return (moeda(x))
    else:
        return (x)


def dobro(num, form=False):
    x = num * 2
    if form == True:
        return(moeda(x))
    else:
        return (x)


def metade(num, form=False):
    x = num / 2
    if form == True:
        return (moeda(x))
    else:
        return (x)

def resumo(num, poraum, pordim):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: {moeda(num)}'
          f'\nDobro: {moeda(num*2)}'
          f'\nMetade: {moeda(num/2)}'
          f'\nAumento de {poraum}%: {moeda(num + (num*(poraum / 100)))}'
          f'\nRedução de {pordim}%: {moeda(num - (num*(pordim / 100)))}')
    print('-'*30)