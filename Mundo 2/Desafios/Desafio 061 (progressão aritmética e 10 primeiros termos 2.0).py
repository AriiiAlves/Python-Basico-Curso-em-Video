termo1 = razão = sinal = res = count = 0
direção = ''
while sinal == 0:
    termo1 = int(input('Primeiro termo da Progressão Aritmética: '))
    razão = int(input('Razão da Progressão Aritmética: '))
    direção = str(input('Direção da razão (+ ou -): '))
    if direção.strip() == '+':
        sinal = 1
    elif direção.strip() == '-':
        sinal = 1
        print(termo1, end=', ')
    else:
        sinal = 0
        print('\nO operador selecionado está incorreto! Digite novamente.\n')
while count < 9 and res >= 0:
    if count == 0:
        print('\n', termo1, end=', ')
    if direção.strip() == '+':
        if termo1 + razão > 0:
            res = termo1 + razão
            print(res, end=', ')
            termo1 = res
            count += 1
    elif direção.strip() == '-':
        if termo1 + razão > 0:
            res = termo1 - razão
            print (res, end= ', ')
            termo1 = res
            count += 1
print('Fim')

