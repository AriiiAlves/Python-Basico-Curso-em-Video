from random import randint
n1 = n2 = mnumb = res = 0
op = 1
while op >= 1 and op <=7:
    mnumb = 0
    op = int(input('\nEscolha a operação desejada'
                   '\n\n[1] Somar'
                   '\n[2] Subtrair'
                   '\n[3] Multiplicar'
                   '\n[4] Dividir'
                   '\n[5] Maior'
                   '\n[6] Menor'
                   '\n[7] Novos números'
                   '\n[8] Sair do programa'
                   '\n\nNúmero da operação:'))
    if op == 7:
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        mnumb = 1
        print(f'\nOs números escolhidos foram {n1} e {n2}')
        input('\nAperte qualquer tecla para continuar')
        op = int(input('\nEscolha a operação desejada'
                       '\n\n[1] Somar'
                       '\n[2] Subtrair'
                       '\n[3] Multiplicar'
                       '\n[4] Dividir'
                       '\n[5] Maior'
                       '\n[6] Menor'
                       '\n[7] Novos números'
                       '\n[8] Sair do programa'
                       '\n\nNúmero da operação:'))
    if mnumb == 0 and op != 8:
        n1 = float(input('\nDigite um número: '))
        n2 = float(input('Digite outro número: '))
    if op == 1 or op == 2 or op == 3 or op == 4 or op == 5 or op == 6:
        mnumb = 0
        if op == 1:
            res = n1 + n2
        if op == 2:
            res = n1 - n2
        if op == 3:
            res = n1 * n2
        if op == 4:
            res = n1 / n2
        if op == 5:
            if n1 > n2:
                res = n1
            elif n2 > n1:
                res = n2
            else:
                res = 'n1 e n2 são iguais.'
        if op == 6:
            if n1 < n2:
                res = n1
            elif n2 < n1:
                res = n2
            else:
                res = 'n1 e n2 são iguais.'
        print(f'\nO resultado é: {res}')
        input('\nAperte qualquer tecla para continuar')
print('\nFim')