termo1 = int(input('Primeiro termo da Progressão Aritmética: '))
razão = int(input('Razão da Progressão Aritmética: '))
direção = str(input('Direção da razão (+ ou -): '))
print()
seq = termo1
termo = 0
sinal = 0
if direção.strip() == '+':
    sinal = 1
    print(termo1, end=', ')
elif direção.strip() == '-':
    sinal = 1
    print(termo1, end=', ')
else:
    sinal = 0
    print('O operador selecionado está incorreto!')
for c in range(0, 9):
    if direção.strip() == '+':
        termo = seq + razão
        if termo >= 0:
            print(termo, end=', ')
    elif direção.strip() == '-':
        termo = seq - razão
        if termo >= 0:
            print(termo, end=', ')
    seq = termo
if sinal == 1:
    print('ACABOU')