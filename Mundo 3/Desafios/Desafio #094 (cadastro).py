dados_pessoa = {}
lista = []
escolha=média=0
while True:
    dados_pessoa['nome'] = str(input('Digite o nome: ')).strip().lower().title()
    dados_pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()
    dados_pessoa['idade'] = int(input('Digite a idade: '))
    lista.append(dados_pessoa.copy())
    escolha = str(input('Deseja realizar mais um cadastro? [S/N]: '))
    if escolha in 'Nn':
        break
# lista = [{'nome': 'Ariel', 'sexo': 'M', 'idade': 16},
#          {'nome': 'Maria', 'sexo': 'F', 'idade': 18},
#          {'nome': 'Jonas', 'sexo': 'M', 'idade': 21}]
print(f'\nForam cadastradas {len(lista)} pessoas.')
for pessoa in lista:
    média += pessoa['idade']
média = média/len(lista)
print(f'Idade média dos cadastrados: {média:.2f}')
print('\nMulheres cadastradas: ', end='')
for pessoa in lista:
        if pessoa['sexo'] in 'Ff':
            print(f'{pessoa["nome"]} ', end='')
print('\nPessoas acima da média cadastradas: ', end='')
for pessoa in lista:
    if pessoa['idade'] > média:
        print(f'{pessoa["nome"]} ', end='')