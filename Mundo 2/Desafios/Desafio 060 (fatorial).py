#!5 = 5 * 4 * 3 * 2 * 1
'''escolha = 's'
prox_f = f = tot = 0
cont = 1
while escolha.strip().lower() == 's':
    n = int(input('Digite um número: '))
    tot = n
    prox_f = 0
    cont = 1
    while prox_f != 1:
        prox_f = n - cont
        f = tot * prox_f
        tot = f
        cont += 1
    print(f'O fatorial de {n} é igual a {tot}')
    escolha = str(input('\nDeseja continuar? [S/N] '))
    print()'''

n = int(input('Digite um número: '))
bo = f = cf = 0
for c in range (1, n):
    if bo == 0:
        f = n * (n - c)
        bo = 1
    else:
        cf = f * (n - c)
        f = cf
print(f'\nO fatorial de {n} é igual a {f}')