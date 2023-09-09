from random import randint
from time import sleep

# Minha solução
# def sorteia(lst):
#     print('Números sorteados: ', end='')
#     for c in range(0, 4):
#             escolha = randint(0, 101)
#             print(escolha, end=', ')
#             lst.append(escolha)
#             sleep(0.5)
#     print('PRONTO!')
#
# def somapar(lst):
#     s = 0
#     print('Somando valores pares de ', end='')
#     for v in lst:
#         print(v, end=', ')
#         if v % 2 == 0:
#             s += v
#         sleep(0.5)
#     print(f'Temos {s}')
#
#
# lista = []
# sorteia(lista)
# somapar(lista)


# Solução de inscrito usando return
def sorteia(lst):
    numeros = []
    c = 0
    while c < 5:
        n = randint(0, 10)
        numeros.append(n)
        c += 1
    return numeros


def somaPar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    return s


lista = []
lista = sorteia(lista)
print(f'Os números sorteados foram {sorteia(lista)}')
print(f'A soma dos pares foi {somaPar(lista)}')


