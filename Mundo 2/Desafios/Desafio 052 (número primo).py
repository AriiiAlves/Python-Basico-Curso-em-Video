#n = int(input('Digite um número: '))
#cont = 0
#for c in range(1, 1000000):
    #if n % c == 0:
        #cont += 1
#if cont <= 2:
    #print(f'\n{n} é um número \033[1;32mprimo.\033[m')
#else:
    #print(f'\n{n} \033[1;31mnão\033[m é um número primo.')

n = 0
cont = 0
for c1 in range(2, 1000001):
    n = c1
    cont = 0
    for c2 in range(1, 1000001):
        if n % c2 == 0:
            cont += 1
    if cont <= 2:
        print(f'{c1} é um número \033[1;32mprimo.\033[m')
print('\nFIM')