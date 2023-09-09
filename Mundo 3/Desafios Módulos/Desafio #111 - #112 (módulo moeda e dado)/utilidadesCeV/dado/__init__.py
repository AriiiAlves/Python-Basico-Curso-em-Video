def leiadinheiro(msg):
    while True:
        num = str(input(msg)).replace(',', '.')
        if num.isalpha():
            print(f'\033[1;31mErro! "{num}" é um preço inválido!\033[m')
        else:
            return (float(num))
            break
