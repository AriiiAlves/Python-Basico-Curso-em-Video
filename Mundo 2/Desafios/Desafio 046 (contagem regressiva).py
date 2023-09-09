from time import sleep
from emoji import emojize
input('Aperte qualquer tecla para começar a contagem regressiva!\n')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize('\nFeliz ano novo! :fireworks:'))