from random import randint, choice

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

#alf = randint(1,4)

#if alf == 1:
    #result = al1
#elif alf == 2:
    #result = al2
#elif alf == 3:
    #result = al3
#elif alf == 4:
    #result = al4

#print(f'Aluno sorteado: {result}')

lista = [al1, al2, al3, al4]

escolhido = choice(lista)

print(f'Aluno sorteado: {escolhido}')