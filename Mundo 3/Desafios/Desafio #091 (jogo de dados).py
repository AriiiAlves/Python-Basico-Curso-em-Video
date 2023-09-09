from random import randint
from time import sleep
from operator import itemgetter
# dados = {}
# all_results = []
# resultado = 0
# for c in range(1, 5):
#     resultado = randint(1, 6)
#     print(f'Jogador {c} tirou: {resultado}')
#     dados['jogador'] = c
#     dados['resultado'] = resultado
#     all_results.append(dados.copy())

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6),}
ranking = {}
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #(0) = ordem de key, (1) = ordem de value
print('\nRanking:')
for c, k in enumerate(ranking):
    print(f'{c+1}° Lugar: {k[0]}')