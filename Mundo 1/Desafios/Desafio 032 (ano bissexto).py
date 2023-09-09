a = int(input('Ditite o ano: '))
print()

if (a%4) == 0:
    print(f'{a} é um ano bissexto.')
else:
    print(f'{a} não é um ano bissexto.')