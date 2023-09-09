#p = tupla inteira
p = ('aumento',
     'lanche',
     'hamburguer',
     'dois',
     'quadrado',
     'elevador',
     'complexo',
     'comando',
     'classificado',
     'a', 'e', 'i', 'o', 'u')
# pi = cada item da tupla separadamente
for pi in p:
    print(f'Vogais de {pi.upper()}: ', end='')
    for letra in pi:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
        # se (if) tiver letradoitempi (letra)  em (in) 'aeiou':
        # escrever (print) (letradoitempi (letra), espaçonofinaldalinha (end=' '))
    print('\n', end='')