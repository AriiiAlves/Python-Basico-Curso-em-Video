npes = int(input('Digite o número de pessoas: '))
s_idades =  0
hmais_velho = ''
maior_idade = 0
s_mul = 0
for c in range(1, npes + 1):
    print(f'Pessoa {c}')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    s_idades += idade
    if sexo.strip().lower() == 'masculino' and idade > maior_idade:
        hmais_velho = nome
        maior_idade = idade
    if sexo.strip().lower() == 'feminino' and idade < 20:
        s_mul += 1
print(f'\nMédia de idade do grupo: {s_idades / npes} anos'
      f'\nHomem mais velho: {hmais_velho.strip().lower().title()}'
      f'\nQuantidade de mulheres com menos de 20 anos: {s_mul}')