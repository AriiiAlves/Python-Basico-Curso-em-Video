from random import randint

n = int(randint(0, 5))

print('\033[1m' + f'Hey, Pssss!! Não conta pra ninguém... O número escolhido foi: {n}', '\033[0m')
print()
choose = int(input('De 0 a 5, adivinhe o número escolhido: '))
print()

if choose == n:
    print('Parabéns, você acertou!')
else:
    print('Puxa, não foi dessa vez... tente novamente!')