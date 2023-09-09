aluno = [[], [[], []]]
lista = []
média = choose = 0
quantidade = int(input('Quantos alunos são: '))
for c in range(1, quantidade + 1):
    aluno[0].append((str(input(f'\nDigite o nome do {c}° aluno: ')).strip().title()))
    aluno[1][0].append(float(input('Digite a 1° nota do aluno: ')))
    aluno[1][1].append(float(input('Digite a 2° nota do aluno: ')))
    lista.append(aluno[:])
    aluno.clear()
    aluno = [[], [[], []]]
#lista = [[['Ariel'], [[10.0], [9.0]]], [['Maria'], [[10.0], [8.0]]]]
print('=-'*5, 'BOLETIM'.center(6), '-='*5)
print('-' *29)
print('N°', f'   ALUNO', f'            MÉDIA')
for n, estudante in enumerate(lista):
    média = (estudante[1][0][0] + estudante[1][1][0])/2
    print(f'{n:<5}', f'{str(estudante[0][0]):<15}', f'{média:>5.1f}')
print('-' *29)
while choose != 999:
    choose = int(input('Deseja mostrar notas de qual aluno? (999 interrompe): '))
    print(f'Notas de {lista[choose][0][0]} são {lista[choose][1][0][0]}, {lista[choose][1][1][0]}')
    print()