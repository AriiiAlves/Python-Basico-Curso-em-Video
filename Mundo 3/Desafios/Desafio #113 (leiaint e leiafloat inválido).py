def leiaInt():
    while True:
        try:
            n = int(input('Digite um número Inteiro: '))
        except Exception as erro:
            print(f'\033[1;31mDigite um número inteiro válido. Erro: {erro}\033[m')
        else:
            return(n)
            break

def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número Real: '))
        except Exception as erro:
            print(f'\033[1;31mDigite um número real válido. Erro: {erro}\033[m')
        else:
            return(n)
            break

def main():
    inteiro = leiaInt()
    real = leiaFloat()
    print(f'\nVocê digitou o número Inteiro {inteiro} e o número Real {real:.2f}')


main()