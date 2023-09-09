#Em qualquer triângulo, a soma das medidas de dois lados é sempre maior que a medida do terceiro.

l1 = int(input('Digite o valor do primeiro lado: '))
l2 = int(input('Digite o valor do segundo lado: '))
l3 = int(input('Digite o valor do terceiro lado: '))
print()

if (l1+l2) > l3 and (l2+l3) > l1 and (l3+l1) > l2:
    tri = True
else:
    tri = False

if tri == True:
    print(f'O triângulo pode ser formado pelas retas {l1}, {l2} e {l3}. \nCombinação possível.')
else:
    print(f'O triângulo não pode ser formado pelas retas {l1}, {l2} e {l3}. \nCombinação impossível.')