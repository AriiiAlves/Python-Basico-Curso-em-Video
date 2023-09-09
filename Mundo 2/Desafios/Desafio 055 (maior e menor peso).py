npes = int(input('Digite o número de pessoas: '))
cont = 0
maior = 0
menor = 0
peso = 0
c1 = 0
pes_maior = 0
pes_menor = 0
for c in range(1, npes + 1):
    peso = float(input(f'Peso {c} em Kg: '))
    if menor == 0:
        menor = 10000000
    if peso > maior:
        maior = peso
        c1 = c
        pes_maior = c1
    if peso < menor:
        menor = peso
        c2 = c
        pes_menor = c2
print(f'\nO maior peso é: {maior} Kg ({pes_maior}° pessoa)'
      f'\nO menor peso é: {menor} Kg ({pes_menor}° pessoa)')