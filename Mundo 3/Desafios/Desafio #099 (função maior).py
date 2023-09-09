from time import sleep

def maior(*num):
    for c, n in enumerate(num):
        if c == 0:
            m = n
        else:
            if n > m:
                m = n
    print('-'*50)
    print('Analisando os valores passados...')
    print(f'Valores: ', end='')
    for n in num:
        print(n, end=' ')
        sleep(0.5)
    print(f'. São {len(num)} valores ao todo.')
    print(f'O maior número é {m}')


maior(1, 2, 3, 4)
maior(12, 124124, 42, 10000, 47000000, 10)
maior(12, 16, 29, 50, 1, -200, 100)