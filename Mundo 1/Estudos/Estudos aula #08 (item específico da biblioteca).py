from math import sqrt, ceil, floor, trunc

num = int(input('Digite um número: '))

raiz = sqrt(num)

print(f'A raiz de {num} é igual a {raiz}')
print(f'A raiz de {num} é igual a {raiz:.2f}')
print(f'A raiz de {num} é igual a {ceil(raiz)}')
print(f'A raiz de {num} é igual a {floor(raiz)}')
print(f'A raiz de {num} é igual a {trunc(raiz)}')