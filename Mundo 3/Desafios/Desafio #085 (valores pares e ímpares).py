lista = []
temp = []
pares = []
ímpares = []
for c in range(0, 7):
    temp.append(int(input('Digite um valor: ')))
    if temp[0] % 2 == 0:
        pares.append(temp[0])
        print('Par adicionado')
    else:
        ímpares.append(temp[0])
        print('Ímpar adicionado')
    temp.clear()
lista.append(pares[:])
lista.append(ímpares[:])
print()
print(f'Valores pares: {sorted(lista[0])}')
print(f'Valores ímpares: {sorted(lista[1])}')
