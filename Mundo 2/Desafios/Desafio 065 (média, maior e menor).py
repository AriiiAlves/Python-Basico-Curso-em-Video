n = s = maior = count = 0
menor = 10000
escolha = 's'
while escolha.strip().lower() == 's':
    n = int(input('Digite um número: '))
    s += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    if menor == 10000:
        menor = n
    count += 1
    escolha = str(input('\nQuer continuar a digitar valores? [S/N]: '))
    print(f'\nMédia entre números lidos: {s / count}'
          f'\nMaior valor lido: {maior}'
          f'\nMenor valor lido: {menor}')
    #Debug
    print(f'\n\nDebug s = {s} count = {count}')
    print()
print('\nFim')