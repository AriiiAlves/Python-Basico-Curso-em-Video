preço = input('Preço do produto: R$ ')
fpreço = float(''.join(preço.strip().replace(',', '.').split()))
condição = int(input('Formas de pagamento:'
                     '\n\n[1] À Vista no dinheiro/cheque'
                     '\n[2] À Vista no cartão'
                     '\n[3] Em até 2x no cartão'
                     '\n[4] Em 3x ou mais no cartão'
                     '\n\nDigite o número da forma de pagamento: '))
if condição == 1:
    forma_pg = 'À Vista no dinheiro/cheque'
    total = fpreço - (fpreço*0.10)
elif condição == 2:
    forma_pg = 'À Vista no cartão'
    total = fpreço - (fpreço*0.05)
elif condição == 3:
    forma_pg = 'Em até 2x no cartão'
    total = fpreço
elif condição == 4:
    forma_pg = 'Em 3x ou mais no cartão'
    total = fpreço + (fpreço*0.20)
else:
    forma_pg = '\033[1;31Erro\033[m'
    total = '\033[1;31Erro\033[m'
print(f'\nForma de pagamento escolhida: {forma_pg}'
      f'\n\nValor a ser pago: R$ \033[0;34m{total}\033[m')