from datetime import datetime
dados = {}
lista = []
ask = 0
while True:
    dados['nome'] = str(input('Digite o Nome: ')).strip().title()
    dados['idade'] = (datetime.now().year - int(input('Digite o Ano de Nascimento: ')))
    dados['carteira de trabalho'] = str(input('Carteira de Trabalho [SIM/NÃO]: ')).strip().title()
    if dados['carteira de trabalho'].lower() in 'sim':
        dados['ano contratação'] = int(input('Digite o Ano de Contratação: '))
        dados['salário'] = float(input('Digite o Salário: '))
        dados['aposentadoria'] = (dados['idade'] + ((dados['ano contratação'] + 35) - datetime.now().year)), 'anos'
    else:
        dados['ano contratação'] = 'None'
        dados['salário'] = 'None'
        dados['aposentadoria'] = 'None'
    lista.append(dados.copy())
    ask = str(input('Deseja cadastrar mais um funcionário? [S/N]: '))
    if ask in 'Nn':
        break
for funcionário in lista:
    print('-' * 32)
    for k, v in funcionário.items():
        print(f'{k}: {v}')
    print('-' * 32)