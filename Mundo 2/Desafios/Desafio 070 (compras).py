n = p = s = cp = pb = 0
an = 10000
while True:
    print('--' * 20)
    n = str(input('Digite o nome do produto: '))
    p = float(input('Digite o preço do produto: '))
    s += p
    if p > 1000:
        cp += 1
    if p < an:
        pb = n
    an = p
    print('--' * 20)
    print(f'Total gasto na compra: R$ {s}'
          f'\nProdutos que custaram mais de R$ 1000: {cp} produto(s)'
          f'\nProduto mais barato: {pb}')
    print('--' * 20)
    a = str(input('Deseja continuar? [S/N]: '))
    if a.strip().upper() == 'N':
        print('--' * 10, 'FIM DO PROGRAMA', '--' * 10)
        break