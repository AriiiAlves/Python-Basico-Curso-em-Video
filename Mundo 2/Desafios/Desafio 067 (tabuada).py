n = f = r = 0
while True:
    print('-' * 20)
    n = int(input('Digite um número: '))
    print('-' * 20)
    if n < 0:
        break
    else:
        f = 0
        while True:
            if f == 0:
                r = n * f
                print(f'{n} * {f} = {r}')
                f += 1
            else:
                f += 1
                r = n * f
                print(f'{n} * {f} = {r}')
            if f == 10:
                break