s = int(input('Digite o salário do funcionário: R$ '))
print()

if s > 1250:
    sf = s+(s*0.10)
    a = '10%'
else:
    sf = s+(s*0.15)
    a = '15%'

print(f'O salário do funcionário recebeu um aumento de {a}, totalizando: R$ {sf}')