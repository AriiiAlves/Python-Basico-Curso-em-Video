from random import shuffle
print()
input('>Bem vindo! Digite abaixo o nome dos alunos para ser sorteada a ordem de apresentação<')

al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))

lista = [al1, al2, al3, al4]

ordem = shuffle(lista)

print(f'A ordem de apresentação será: {lista}')