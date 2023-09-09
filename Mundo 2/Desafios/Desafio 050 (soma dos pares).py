#s = 0
#for c in range (0, 6):
    #n = int(input('Digite um número: '))
    #if (n % 2) == 0:
        #s += n
#print(f'\nSoma dos pares: \033[0;34m{s}\033[m')

s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'\nVocê informou {cont} número(s) PAR(es) e a soma foi \033[0;34m{s}\033[m')