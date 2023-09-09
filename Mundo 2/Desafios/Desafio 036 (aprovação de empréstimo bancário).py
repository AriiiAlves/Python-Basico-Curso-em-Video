vcasa = (input('Valor da casa: R$ '))
vsal = (input('Salário do comprador: R$ '))
anos = (input('Quantos anos de financiamento: '))
meses = (input('Quantos meses a mais: '))
#meses = (input('Em quantos meses o comprador irá pagar o valor da casa:'))


fvcasa = float(''.join(vcasa.strip().replace(',', '.').split()))
fvsal = float(''.join(vsal.strip().replace(',', '.').split()))
fanos = float(''.join(anos.strip().replace(',', '.').split()))
fmeses = float(''.join(meses.strip().replace(',', '.').split()))

vmen = fvcasa / ((fanos*12)+fmeses)
#vmen = fvcasa / fmeses

if vmen <= fvsal*0.30:
    print('\nParabéns, o empréstimo foi \033[0;32maprovado!\033[m')
else:
    print('\nSinto muito, o empréstimo foi \033[0;31mnegado.\033[m')

print(f'\nValor do salário: R$ {fvsal:.2f}'
      f'\nValor da mensalidade: R$ {vmen:.2f}')