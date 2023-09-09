termo1 = razão = sinal = sinal2 = variável_fixa = res = count = count2 = count3 = count4 = controle = 0
n_termos = 1
direção = ''
while sinal == 0:
    termo1 = int(input('Primeiro termo da Progressão Aritmética: '))
    razão = int(input('Razão da Progressão Aritmética: '))
    direção = str(input('Direção da razão (+ ou -): '))
    if direção.strip() == '+':
        sinal = 1
    elif direção.strip() == '-':
        sinal = 1
    else:
        sinal = 0
        print('\nO operador selecionado está incorreto! Digite novamente.')
    variável_fixa = termo1
    if direção.strip() == '+' or direção.strip() == '-':
        while count < 9 and res >= 0 and sinal2 == 0:
            if count == 0:
                print('\n', termo1, end=', ')
            if direção.strip() == '+':
                if termo1 + razão > 0:
                    res = termo1 + razão
                    if res >= 0:
                        print(res, end=', ')
                    termo1 = res
                    count += 1
            elif direção.strip() == '-':
                if termo1 + razão > 0:
                    res = termo1 - razão
                    if res >= 0:
                        print(res, end=', ')
                    termo1 = res
                    count += 1
        print('...')
        if count == 9:
            #loop para definir se a PA vai continuar ou não
            while n_termos > 0:
                if count4 == 1:
                    print('...')
                n_termos = int(input('\nQuantos termos a mais você quer que sejam mostrados?'
                                 '\n\nDigite o número de termos: '))
                #debug
                #print(f'\nn termos: {n_termos}')
                #se n_termos for > 0, continua a PA. Se não, encerra o loop while
                if n_termos > 0:
                    sinal2 = 0
                    termo1 = variável_fixa
                    res = count = count2 = 0
                    count4 = 1
                    if count4 == 1:
                        count3 += n_termos
                    #debug 2
                    #print('\n\ncount3: ', count3)
                    #problema está na quantidade de repetições do loop (na soma entre n_termos e count 3), valor errado
                    #RESOLVIDO: n_termos + count3 está errado. Somente count3 (valor agregado dos termos) deve ser usado.
                    while count2 != count3 and res >= 0:
                        while count < 9 and res >= 0:
                            if count == 0:
                                print('\n', termo1, end=', ')
                            if direção.strip() == '+':
                                if termo1 + razão > 0:
                                    res = termo1 + razão
                                    if res >= 0:
                                        print(res, end=', ')
                                    termo1 = res
                                    count += 1
                            elif direção.strip() == '-':
                                if termo1 + razão > 0:
                                    res = termo1 - razão
                                    if res >= 0:
                                        print(res, end=', ')
                                    termo1 = res
                                    count += 1
                        if direção.strip() == '+':
                            if termo1 + razão > 0:
                                res = termo1 + razão
                                if res >= 0:
                                    print(res, end=', ')
                                termo1 = res
                                count2 += 1
                        elif direção.strip() == '-':
                            if termo1 + razão > 0:
                                res = termo1 - razão
                                if res >= 0:
                                    print(res, end=', ')
                                termo1 = res
                                count2 += 1
                    #debug 3
                    '''print('\n\nn_termos: ', n_termos)
                    print('count2: ', count2)
                    print('count3: ', count3, '\n')'''
                else:
                    sinal2 = 1
print('\nFim')