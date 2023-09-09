'''frase = str(input('Digite uma frase: '))
ffrase = ''.join(frase.strip().lower().split())
inv = ffrase[::-1]
print(f'\nO inverso de {ffrase} é {inverso}')
if ffrase == inv:
    print('A frase é um \033[1;32mpalíndromo.\033[m')
else:
    print('A frase \033[1;31mnão\033[m é um palíndromo.')'''

frase = str(input('Digite uma frase: '))
ffrase = ''.join(frase.strip().upper().split())
inverso = ''
for letra in range(len(ffrase) -1, -1, -1):
    # (len(ffrase) -1, -1, -1): calcula o tamanho da frase inteira e tira 1 para igualar aos caracteres (len vai do 1-x, e caracteres vão do 0-x) e dar o valor do INÍCIO. Assim, uma frase com len = 20 vai ter 19 caracteres.
    #depois, o FIM é definido como -1 (antes do primeiro caractere)
    #por fim, a ordem é inversa (-1), começando do -1 e indo até o caractere especificado por (len(ffrase) -1).
    inverso += ffrase[letra]
    #aqui, [letra] seleciona o caractere da frase a ser utilizado. Com o loop, vão sendo pegadas as letras de trás para frente, formando a frase na ordem inversa.
#print(inverso)
print(f'\nO inverso de {ffrase} é {inverso}')
if inverso == ffrase:
    print(f'A frase é um \033[1;32mpalíndromo.\033[m')
else:
    print('A frase \033[1;31mnão\033[m é um palíndromo.')