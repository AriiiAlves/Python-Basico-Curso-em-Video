'''n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
n4 = int(input('Digite um número:'))'''

'''n1=n2=n3=n4=0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    if c == 0:
        n1 = n
    if c == 1:
        n2 = n
    if c == 2:
        n3 = n
    if c == 3:
        n4 = n

tn = (n1, n2, n3, n4)'''

tn = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print('=-' * 20)
if 9 in tn:
    print(f'O valor 9 apareceu {tn.count(9)} vezes.')
else:
    print('O valor 9 não foi digitado em nenhuma posição')
if 3 in tn:
    print(f'O primeiro valor 3 foi digitado na {(tn.index(3)) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os números pares digitados foram: ', end='')
for n in tn:
    if n % 2 == 0:
        print(n, end=' ')
print('\n' + ('=-' * 20))

