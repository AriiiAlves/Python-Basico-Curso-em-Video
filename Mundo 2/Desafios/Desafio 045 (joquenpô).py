from random import randint
choose = int(input('Bem vindo ao Joquenpô! Será que você consegue ganhar da máquina?'
                   '\n\n[1] para PEDRA'
                   '\n[2] para PAPEL'
                   '\n[3] para TESOURA'
                   '\n\nFaça sua escolha: '))
mchoose = randint(1,3)
if choose == 1:
    escolha = 'PEDRA'
elif choose == 2:
    escolha = 'PAPEL'
elif choose == 3:
    escolha = 'TESOURA'
else:
    escolha = '\033[0;31mErro\033[m'
if mchoose == 1:
    mescolha = 'PEDRA'
elif mchoose == 2:
    mescolha = 'PAPEL'
elif mchoose == 3:
    mescolha = 'TESOURA'
if (mchoose == 1 and choose == 3) or (mchoose == 2 and choose == 1) or (mchoose == 3 and choose == 2):
    resultado = 'Você PERDEU.'
elif (choose == 1 and mchoose == 3) or (choose == 2 and mchoose == 1) or (choose == 3 and mchoose == 2):
    resultado = 'Você GANHOU.'
elif mchoose == choose:
    resultado = 'EMPATE.'
else:
    resultado = '\033[0;31mErro\033[m'
print(f'\nVocê jogou: {escolha}'
      f'\nA máquina jogou: {mescolha}'
      f'\n\n{resultado}')