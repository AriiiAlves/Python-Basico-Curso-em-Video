lista = []
for c in range(0, 5):
    n = int(input(f'Digite um valor para a posição {c}: '))
    lista += [n]
print('=-' * 40)
print(f'Você digitou os valores {lista}'
      f'\nO maior valor digitado foi {max(lista)} nas posições ', end='')
for contagem, numero in enumerate(lista):
    if numero == max(lista):
        print(contagem, end='...')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end ='')
for contagem, numero in enumerate(lista):
    if numero == min(lista):
        print(contagem, end='...')
print()