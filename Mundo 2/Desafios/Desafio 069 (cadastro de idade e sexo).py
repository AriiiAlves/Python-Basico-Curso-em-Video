n = i = s = ci = cs = cm = 0
while True:
    n = str(input('Digite o nome: '))
    i = int(input('Digite a idade: '))
    s = str(input('Digite o sexo [M/F]: '))
    if i > 18:
        ci += 1
    if s.strip().upper() == 'M':
        cs += 1
    if s.strip().upper() == 'F' and i < 20:
        cm += 1
    print('--' *15)
    print(f'Maiores de 18 anos: {ci} pessoa(s)'
          f'\nHomens: {cs} pessoa(s)'
          f'\nMulheres menores de 20 anos: {cm} pessoa(s)')
    print('--' * 15)
    a = str(input('Gostaria de continuar? [S/N]: '))
    print('--' * 15)
    if a.strip().upper() == 'N':
        break
