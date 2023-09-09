ano_nasc = int(input('Informe seu ano de nascimento: '))
ano_atual = 2022
idade = ano_atual - ano_nasc
if idade < 18:
    print(f'\nMenor de 18 anos, deverá fazer o alistamento militar. Tempo restante: {18 - idade} anos.')
elif idade == 18:
    print('\n18 anos, está na hora de fazer o alistamento militar.')
else:
    print(f'\nJá passou o tempo do alistamento. Prazo vencido em {idade - 18} anos.')