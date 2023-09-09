d = int(input('Qual a distância da viagem em Km? '))
print()

if d <= 200:
    print(f'A viagem é curta. O valor estipulado da passagem é de {d*0.5}')
else:
    print(f'A viagem é longa. O valor estipulado da passagem é de {d*0.45}')