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
#c=0
for pi in p:
    print(f'Vogais de {pi.upper()}: ', end='')
    '''if pi.lower().count('a') >= 1:
        c = pi.lower().count('a')
        for n in range(0, c):
            print('a', end='  ')
    if pi.lower().count('e') >= 1:
        c = pi.lower().count('e')
        for n in range(0, c):
            print('e', end='  ')
    if pi.lower().count('i') >= 1:
        c = pi.lower().count('i')
        for n in range(0, c):
            print('i', end='  ')
    if pi.lower().count('o') >= 1:
        c = pi.lower().count('o')
        for n in range(0, c):
            print('o', end='  ')
    if pi.lower().count('u') >= 1:
        c = pi.lower().count('u')
        for n in range(0, c):
            print('u', end='  ')'''
    for vogal in pi:
        #if vogal.lower() in 'aeiou':
        if 'a' in vogal.lower():
            print(vogal, end=' ')
    print('\n', end='')