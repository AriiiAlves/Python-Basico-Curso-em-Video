n = int(input('Digite quantos termos da Sequência de Fibonacci você quer ver: '))
count = leitura = valor1 = valor2 = 0
while count != n:
    if count == 0:
        print(0, end=' ➝ ')
        print(1, end=' ➝ ')
        valor1 = 0
        valor2 = 1
    leitura = valor1 + valor2
    valor1 = valor2
    valor2 = leitura
    print(leitura, end=' ➝ ')
    count += 1
print('Fim')
