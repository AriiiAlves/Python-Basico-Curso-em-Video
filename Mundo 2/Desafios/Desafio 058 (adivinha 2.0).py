from random import randint
mnumb = 0
cnumb = 11
erro = 0
n_tent = 1
while mnumb != cnumb:
    mnumb = randint(0, 10)
    if erro == 0:
        cnumb = int(input('Tente adivinhar o número que estou pensando... Está entre 0 e 10!'
                      '\nDigite o número escolhido: '))
    else:
        cnumb = int(input('Digite o número escolhido: '))
    if mnumb != cnumb:
        print(f'Putz, você errou... O número que eu estava pensando era {mnumb}. Tente novamente!\n')
        erro = 1
        n_tent += 1
print('\nParabéns, você acertou!'
      f'\nPalpites necessários pra vencer: {n_tent}')