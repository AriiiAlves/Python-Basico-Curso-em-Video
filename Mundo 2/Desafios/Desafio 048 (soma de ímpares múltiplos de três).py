s = 0
for c in range(1, 500, 2):
    if (c % 3) == 0:
        s += c
print(f'Soma de todos os números ímpares múltiplos de três entre 1-500: \033[0;34m{s}\033[m')