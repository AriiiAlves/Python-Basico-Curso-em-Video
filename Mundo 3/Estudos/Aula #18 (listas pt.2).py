'''dados = ['Pedro', 25]
dados1 = ['Maria', 19]
dados2 = ['João', 32]
pessoas = [dados[:], dados1[:], dados2[:]]
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
pessoas.append(dados[:])
print(dados)
print(pessoas)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 25]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

#estrutura principal
galera = list()
#estrutura auxiliar
dado = list()
#definição de variáveis simples
totmai = totmen = 0
#leitura de dados para formar a lista
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
#análise de dados e apresentação de informações
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Total de maiores = {totmai}')
print(f'Total de menores = {totmen}')
