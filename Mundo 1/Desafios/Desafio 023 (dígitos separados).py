num = (input('Digite um número de 0 a 9999: '))

print()

fnum = num.strip()

print(f'Unidade: {fnum[0]}')
print(f'Dezena: {fnum[1]}')
print(f'Centena: {fnum[2]}')
print(f'Milhar: {fnum[3]}')