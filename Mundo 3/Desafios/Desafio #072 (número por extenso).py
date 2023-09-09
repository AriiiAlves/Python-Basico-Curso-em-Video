n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    e = int(input('Digite um número entre 0 e 20: '))
    if e >= 0 and e <= 20:
        print(f'Você digitou o número {n[e]}')
        break
    else:
        print('Tente novamente.', end = ' ')

