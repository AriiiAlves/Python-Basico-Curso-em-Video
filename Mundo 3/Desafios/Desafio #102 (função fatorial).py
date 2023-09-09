from time import sleep


def fatorial(num, show=False):
    """num: Número para calcular seu fatorial
    show=False/True: Opção para mostrar a conta completa ou não

    Em ambos os casos, será retornado o resultado do fatorial"""
    ant = 1
    for n in range(1, num + 1):
        fat = n
        fat *= ant
        ant = fat
    if show:
        for n in range(1, num + 1):
            if n != num:
                print(n, end=' x ', flush=False)
            else:
                print(f'{n} = ', end='', flush=False)
                return (fat)
            # sleep(0.5)
    else:
        # print(f'O fatorial de {num} é igual a {fat}')
        return (fat)


fatorial(10, show=False)
print(fatorial(10, show=True))
print(fatorial(10) + 1)
help(fatorial)