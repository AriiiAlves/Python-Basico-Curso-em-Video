'''listagem = while True:
    str(input('Digite um produto: ')), float(input('Digite seu preço: '))
    n = str(input('Deseja colocar mais um produto? [S/N]: '))
    if n.strip().upper() == 'N':
        break'''

'''listagem = (str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')),
            str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')),
            str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')),
            str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')),
            str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')),
            str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')),
            str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')),
            str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')),
            str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')),
            str(input('Digite um produto: ')),
            float(input('Digite seu preço: ')))'''
listagem = ('lápis', 1.75, 'borracha', 2, 'caderno', 15.90, 'estojo', 25, 'transferidor', 4.2, 'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.3, 'livro', 34.9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for n in listagem:
    if listagem.index(n) % 2 == 0:
        print(f'{n.strip().title():.<30}', end='')
        #print(f'{n.strip().title():< + (".") * 30}', end='')
    if listagem.index(n) % 2 != 0:
        #print(f'R${n:>7.2f}', end='')
        print(f'R${n:>7.2f}')
print('-' * 40)