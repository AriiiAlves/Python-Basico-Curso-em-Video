v = C50 = C20 = C10 = C1 = VA = 0
print('=' * 10, 'BANCO DO BRASIL', '=' * 10)
while True:
    v = int(input('Valor a ser sacado: '))
    VA = v
    if v >= 50:
        C50 = v // 50
        VA = v - (C50 * 50)
        '''print(f'C50: {C50}')
        print(f'VA: {VA}')'''
    if VA >= 20:
        C20 = VA // 20
        VA = VA - (C20 * 20)
        '''print(f'C20: {C20}')
        print(f'VA: {VA}')'''
    if VA >= 10:
        C10 = VA // 10
        VA = VA - (C10 * 10)
        '''print(f'C10: {C10}')
        print(f'VA: {VA}')'''
    if VA >= 1:
        C1 = VA // 1
    print(f'\nTotal de {C50} cédulas de R$ 50'
          f'\nTotal de {C20} cédulas de R$ 20'
          f'\nTotal de {C10} cédulas de R$ 10'
          f'\nTotal de {C1} moedas de R$ 1')
    print('==' * 20)
    print('Volte sempre ao BANCO DO BRASIL, tenha um bom dia.')
    break