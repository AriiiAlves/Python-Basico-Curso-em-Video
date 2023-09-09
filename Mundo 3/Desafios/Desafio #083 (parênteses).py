lista = input('Digite a expressão: ')
for caractere in lista:
    lista += caractere
if lista.count('(') == lista.count(')'):
    print('A expressão é válida')
else:
    print('Sua expressão está errada!')