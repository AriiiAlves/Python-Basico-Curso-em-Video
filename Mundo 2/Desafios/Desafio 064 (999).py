n = count = s = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        count += 1
        s += n
print(f'\nForam digitados {count} números'
      f'\nA soma dos números digitados é igual a {s}')