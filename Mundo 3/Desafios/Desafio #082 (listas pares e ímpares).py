lista = []
lista_pares = []
lista_impares = []
while True:
    n = (int(input('Digite um valor numérico: ')))
    lista += [n]
    resposta = str(input('Deseja continuar? [Enter para S, N para parar]: '))
    if resposta.strip().upper() == 'N':
        break
for numero in lista:
    if numero % 2 == 0:
        lista_pares += [numero]
    else:
        lista_impares += [numero]
print(f'\nLista principal: {lista}'
      f'\nPares na lista: {lista_pares}'
      f'\nPares na lista: {lista_impares}')