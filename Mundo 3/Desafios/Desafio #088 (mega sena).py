from random import randint
resultado_jogo = []
todos_jogos = []
print('*'*40)
print('BEM VINDO AO SORTEADOR DA MEGA SENA!'.center(40))
print('*'*40, '\n')
n_jogos = int(input('Quantos jogos serão gerados: '))
for c in range(0, n_jogos):
    for c1 in range(0, 6):
        resultado_jogo.append(randint(1, 61))
    todos_jogos.append(resultado_jogo[:])
    resultado_jogo.clear()
print()
print('-='*6, f'SORTEANDO {n_jogos} JOGOS'.center(16), '=-' *6, '\n')
for c in range(0, n_jogos):
    print(f'Números para o jogo {c+1}: ', end='')
    print(todos_jogos[c])
print()
print('-='*8, f'BOA SORTE!'.center(8), '=-' *8)