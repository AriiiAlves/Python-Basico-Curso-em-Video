from random import randint
n = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
'''for c in n:
    if c > nrma:
        nrma = c
    if c < nrme:
        nrme = c'''
#print(f'Números gerados: {n}')
print('Os valores sorteados foram:', end=' ')
for pn in n:
    print(f'{pn}', end=', ')
print(f'\nMaior valor: {max(n)}')
print(f'Menor valor: {min(n)}')