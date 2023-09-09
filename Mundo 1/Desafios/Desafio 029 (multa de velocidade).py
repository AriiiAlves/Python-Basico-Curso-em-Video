v = int(input('Velocidade do carro em Km/h: '))
print()

vlim = 80
multa = (v - vlim)*7

if v > vlim:
    print(f'O carro ultrapassou a velocidade limite. A multa estipulada é de: R$ {multa:.2f}')
else:
    print(f'Parabéns, o carro está dentro da velocidade limite de {vlim} Km/h.')