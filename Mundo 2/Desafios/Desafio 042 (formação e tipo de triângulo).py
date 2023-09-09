print('Digite abaixo o valor dos 3 lados do triângulo em metros\n')
l1 = float(input('lado 1: '))
l2 = float(input('lado 2: '))
l3 = float(input('lado 3: '))
if (l1 + l2) > l3 and (l1 + l3) > l3 and (l2 + l3) > l1:
    possível = 'True'
    print('\nO triângulo pode ser formado.\n')
else:
    possível = 'False'
if possível == 'True' and l1 == l2 and l1 == l3 and l2 == l3:
    print('O triângulo é Equilátero.')
elif possível == 'True' and l1 == l2 or l1 == l3 or l2 == l3:
    print('O triângulo é Isósceles.')
elif possível == 'True':
    print('O triângulo é Escaleno.')
else:
    print('O triângulo não pode ser formado.')
