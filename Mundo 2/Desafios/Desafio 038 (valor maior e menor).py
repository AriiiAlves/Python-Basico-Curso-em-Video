n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'\nO primeiro valor (\033[0;34m{n1}\033[m) é maior.')
elif n2 > n1:
    print(f'\nO segundo valor (\033[0;33m{n2}\033[m) é maior.')
else:
    print(f'\nNão existe valor maior, os valores {n1} e {n2} são iguais.')