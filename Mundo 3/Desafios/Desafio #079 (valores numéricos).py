lista = []
while True:
    n = (int(input('Digite um valor numérico: ')))
    if (n in lista) == False:
        lista += [n]
    lista.sort()
    resposta = str(input('Deseja continuar? [Enter para S, N para parar]: '))
    if resposta.strip().upper() == 'N':
        break
print('Valores digitados: ', end='')
for contagem, numero in enumerate(lista):
    if contagem != len(lista) - 1:
        print(f'{numero}, ', end='')
    else:
        print(f'{numero}.')
