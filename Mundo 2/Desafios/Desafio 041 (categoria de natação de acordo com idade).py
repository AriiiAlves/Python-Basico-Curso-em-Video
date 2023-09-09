ano_nasc = (int(input('Informe seu ano de nascimento: ')))
ano_atual = 2022
idade = 2022 - ano_nasc
if idade <= 9:
    print('\nCategoria MIRIM')
elif idade > 9 and idade <= 14:
    print('\nCategoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('\nCategoria JÚNIOR')
else:
    print('\nCategoria MASTER')