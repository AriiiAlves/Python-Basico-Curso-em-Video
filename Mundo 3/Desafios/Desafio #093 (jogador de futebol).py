jogador = {}
partidas = []
p=média=0
jogador['nome'] = str(input('Qual o nome do jogador: ')).strip().lower().title()
p = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(1, p + 1):
    partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c}: ')))
jogador['gols por partida'] = partidas[:]
for gols in partidas:
    média += gols
média = média/p
print(f'\n{jogador["nome"]} fez uma média de {média:.2f} G/P')
print('\nTabela completa\n')
for c, gols in enumerate(partidas):
    print(f'Partida {c+1}: {gols} Gols.')