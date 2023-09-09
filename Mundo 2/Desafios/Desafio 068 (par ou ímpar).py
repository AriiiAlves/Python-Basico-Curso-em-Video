from random import randint
pi = j = m = r = pir = c = 0
while True:
    print('=-' * 15)
    pi = str(input('Você escolhe PAR ou ÍMPAR: '))
    j = int(input('Digite um número: '))
    if pi.strip().lower() == 'par' or pi.strip().lower() == 'ímpar':
        m = randint(1, 100)
        if (j + m) % 2 == 0:
            pir = 'PAR'
        else:
            pir = 'ÍMPAR'
        if pi.strip().lower() == 'par':
            if (j + m) % 2 == 0:
                r = 0
            else:
                r = 1
        if pi.strip().lower() == 'ímpar':
            if (j + m) % 2 != 0:
                r = 0
            else:
                r = 1
    else:
        print('Digite par/ímpar corretamente.')
    print('--' * 15)
    print(f'Você jogou {j} e o computador {m}. Total de {j+m} deu {pir}')
    print('--' * 15)
    if r == 0:
        print('Vitória')
        print('Jogue novamente.')
        c += 1
    else:
        print('Derrota')
        print(f'{c} vitória(s) consecutiva(s).')
        break