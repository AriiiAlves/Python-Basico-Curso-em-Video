from datetime import datetime

def voto(ano):
    global idade
    idade = datetime.now().year - ano
    if idade > 18 and idade < 70:
        return('Obrigatório')
    elif (idade >= 16 and idade <= 18) or (idade > 70):
        return('Opcional')
    else:
        return('Negado')


ano=idade=0
while True:
    ano = int(input('Insira seu ano de nascimento: '))
    voto(ano)
    print(f'Sua idade: {idade}. Seu voto é: {voto(ano)}')
    print('-'*39)