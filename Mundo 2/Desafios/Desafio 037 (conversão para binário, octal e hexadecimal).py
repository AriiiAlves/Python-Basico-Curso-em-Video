nvermelho = '\033[1;31m'
verde = '\033[0;32m'
amarelo = '\033[1;33m'
roxo = '\033[0;35m'
azul = '\033[0;34m'
limpa = '\033[m'
n = int(''.join(input('Digite um número inteiro: ').strip().split()))
base = str(input('Qual será a base de conversão?'
                 f'\n\n[1] para {verde}Binário{limpa}'
                 f'\n[2] para {roxo}Octal{limpa}'
                 f'\n[3] para {azul}Hexadecimal{limpa}'
                 '\n\nBase escolhida: '))
fbase = base.strip()
if base == '1':
    nbase = "Binário"
    cor = verde
    res = bin(n).replace('0b', '')
elif base == '2':
    nbase = "Octal"
    cor = roxo
    res = oct(n).replace('0o', '')
elif base == '3':
    nbase = "Hexadecimal"
    cor = azul
    res = (hex(n)).replace('0x', '')
else:
    nbase = "?"
    cor = nvermelho
    res = 'Erro!'
print(f'\nConversão de {amarelo}{n}{limpa} para {cor}{nbase}{limpa}'
      f'\nResultado: {cor}{res}{limpa}')