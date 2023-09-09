jogador = {}
partidas = []
all_players = []
p=escolha=total=média=0
# while True:
#     jogador['nome'] = str(input('Qual o nome do jogador: ')).strip().lower().title()
#     p = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
#     for c in range(1, p + 1):
#         partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c}: ')))
#     jogador['gols por partida'] = partidas[:]
#     for gols in partidas:
#         total += gols
#     média = total / p
#     jogador['total gols'] = total
#     jogador['média gols'] = média.2f
#     print(jogador)
#     all_players.append(jogador.copy())
#     print(all_players)
#     total = 0
#     média = 0
#     partidas.clear()
#     escolha = str(input('Deseja cadastrar mais um jogador? [S/N]: '))
#     if escolha in 'Nn':
#         break
all_players = [{'nome': 'Rodinei', 'gols por partida': [0, 1], 'total gols': 1, 'média gols': 0.5},
               {'nome': 'Jonas', 'gols por partida': [3, 2], 'total gols': 5, 'média gols': 2.5},
               {'nome': 'Ariel', 'gols por partida': [1, 1, 2], 'total gols': 4, 'média gols': 1.33}]
print('-'*39)
print('Cod Nome        N° Partidas Gols(total)')
for c, player in enumerate(all_players):
    print(f'{(c+1):<4}{player["nome"]:<12}{len(player["gols por partida"]):<12}{player["total gols"]:<11}')
print('-'*39)
while True:
    choose = int(input('Deseja ver as estatísticas de qual jogador (Cod) (0 para): '))
    if choose == 0:
        break
    choose = choose-1
    print('-'*46)
    print('Cod Nome        N°Partidas Gols(total) Gols(média)')
    print(f'{choose:<4}{all_players[choose]["nome"]:<12}{len(all_players[choose]["gols por partida"]):<11}{all_players[choose]["total gols"]:<12}{all_players[choose]["média gols"]:<12}')
    print('\nGols em cada partida')
    for c in range(0, len(all_players[choose]["gols por partida"])):
            print(f'Partida {c+1}: {all_players[choose]["gols por partida"][c]} Gols.')
    print('-'*46)
