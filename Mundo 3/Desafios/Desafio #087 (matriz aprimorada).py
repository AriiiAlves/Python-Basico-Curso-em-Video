matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#matriz = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
somapares = soma3 = mai2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for cont, l in enumerate(matriz):
    for c in l:
        if c % 2 == 0:
            somapares += c
        if l.index(c) == 2:
            soma3 += c
        if cont == 1:
            mai2 = max(l)
print()
print(f'Soma dos pares = {somapares}')
print(f'Soma da 3° coluna = {soma3}')
print(f'Maior valor 2° linha = {mai2}')
