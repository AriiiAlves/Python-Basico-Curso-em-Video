dados = {}
lista = []
ask=0
while True:
    dados['aluno'] = str(input('Digite o nome do aluno: ')).strip().title()
    dados['média'] = float(input('Digite a média do aluno: '))
    if dados['média'] >= 6:
        dados['situação'] = 'Aprovado'
    else:
        dados['situação'] = 'Reprovado'
    lista.append(dados.copy())
    ask = str(input('Deseja registrar mais um aluno? [S/N]: '))
    if ask in 'Nn':
        break
print('-'*38)
print('ALUNO          MÉDIA          SITUAÇÃO')
for info in lista:
    print(f'{info["aluno"]:<15}{info["média"]:<15.2f}{info["situação"]:<10}')
print('-'*38)