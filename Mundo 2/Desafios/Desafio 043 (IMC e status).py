peso = input('Digite seu peso em Kg: ')
altura = input('Digite sua altura em metros: ')
fpeso = float(''.join(peso.strip().replace(',', '.').split()))
faltura = float(''.join(altura.strip().replace(',', '.').split()))
imc = fpeso/(faltura**2)
if imc < 18.5:
    status = 'Abaixo do peso.'
elif imc >= 18.5 and imc < 25:
    status = 'Peso ideal.'
elif imc >= 25 and imc < 30:
    status = 'Sobrepeso.'
elif imc >= 30 and imc < 40:
    status = 'Obesidade.'
else:
    status = 'Obesidade mórbida.'
print(f'\nIMC: {imc:.2f}\nSeu status atual é: {status}')