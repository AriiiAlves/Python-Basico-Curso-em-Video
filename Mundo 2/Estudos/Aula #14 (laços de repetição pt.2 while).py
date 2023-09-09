'''for c in range(1, 10):
    print(c, end=', ')
print('Fim')'''

'''c = 1
while c < 10:
    print(c, end=', ')
    c += 1
print('Fim')'''

'''for c in range(1, 5):
    n = int(input('Digite um número: '))
print('Fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')'''

'''r = 'S'
while r.strip().upper() == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] '))
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'\nVocê digitou {par} números pares e {impar} números ímpares!')