from time import sleep

def contador(a, z, m):
    print(f'Contagem de {a} até {z} de {m} em {m}:', end=' ')
    if z > a:
        z += 1
    if z < a:
        z -= 1
    if m == 0:
        print(0)
    else:
        for c in range(a, z, m):
            if c != 'None':
                print(c, end=' ')
                sleep(0.5)
    print()
    print('-' * 60)

contador(1, 11, 1)
contador(10, 0, -2)
while True:
    a = int(input('Digite o número inicial: '))
    z = int(input('Digite o número final: '))
    m = int(input('Digite o passo (modo de contagem): '))
    print()
    contador(a, z, m)