n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))

#op = input('Digite o símbolo da operação')

#op = {
    #'+': lambda n1, n2: n1 + n2,
    #'-': lambda n1, n2: n1 - n2,
    #'*': lambda n1, n2: n1 * n2,
    #'/': lambda n1, n2: n1 / n2,
    #'**': lambda n1, n2: n1 ** n2,
    #'//': lambda n1, n2: n1 // n2,
    #'%': lambda n1, n2: n1 % n2,
#}

#print(f'{n1}{op}{n2}={op}')

som = n1+n2
sub = n1-n2
mul = n1*n2
div = n1/n2
pot = n1**n2
divin = n1//n2
res = n1%n2

print(' ')
print(f'A soma é {som:.2f}, \n a subtração é {sub:.2f}, \n a multiplicação é {mul:.2f} e \n a divisão é {div:.2f}.', end='>>><<<')
print(f'A potência é {pot:.2f}, a divisão inteira é {divin:.2f} e o resto é {res:.2f}')