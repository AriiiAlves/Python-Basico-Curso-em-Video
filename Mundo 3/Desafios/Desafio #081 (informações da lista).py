lista = []
while True:
    n = (int(input('Digite um valor numérico: ')))
    lista += [n]
    resposta = str(input('Deseja continuar? [Enter para S, N para parar]: '))
    if resposta.strip().upper() == 'N':
        break
lista.sort(reverse=True)
print(f'\nforam digitados {len(lista)} números')
print(f'Lista de valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')

