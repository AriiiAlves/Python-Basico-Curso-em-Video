from statistics import mean

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

med = mean([n1, n2, n3, n4])
print()
print('Nota de corte: 6')
print(f'Média anual obtida: {med}')
print()

if med >= 6:
    print('Aprovado!')
else:
    print('Reprovado.')