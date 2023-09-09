npes = int(input('Digite o número de pessoas: '))
ano_atual = 2023
cont = 0
for c in range(1, npes + 1):
    ano = int(input(f'Data de nascimento {c}: '))
    if (ano_atual - ano) < 21:
        cont += 1
print(f'\n{cont} pessoas ainda não atingiram a maioridade.'
      f'\n{npes - cont} pessoas já são maiores.')