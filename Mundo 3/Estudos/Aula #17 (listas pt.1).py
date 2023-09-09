#lanche = ['lanche', 'suco', 'pizza', 'pudim']
#lanche.append('cookie')
#lanche.insert(0,'cachorro-quente')
#del lanche[3]
#lanche.pop(3)
#lanche.remove('pudim')
# if 'pizza' in lanche:
#     lanche.remove('pizza')
# print(lanche)
# valores = list(range(4, 11))
# print(valores)
# valores = [8, 2, 5, 4, 9, 3, 0]
# print(len(valores))
# print(num)

# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
## for v in valores:
##     print(f'{v} (índice {valores.index(v)})...', end=' ')
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')

# for c, r in enumerate(range(1, 5)):
#     print(c, r)

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
