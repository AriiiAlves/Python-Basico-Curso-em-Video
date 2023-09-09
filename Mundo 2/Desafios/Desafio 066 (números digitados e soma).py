n = s = q = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    q += 1
print(f'Foram digitados {q} números, e sua soma vale {s}')