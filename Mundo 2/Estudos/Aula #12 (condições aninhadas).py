nome = str(input('Digite seu nome: '))
if nome.lower().strip() == 'ariel':
    print(f'\nUau, que nome maravilhoso \033[1;36m{nome.title()}\033[m!')
elif nome.lower().strip() == 'jonas':
    print(f'\nUau, nome brabo hein \033[1;35m{nome.title()}\033[m!')
elif nome.lower().strip() in 'moisés joão pedro paulo noé abel':
    print(f'\nWoww... Nome bíblico! Dahora hein, \033[1;34m{nome.title()}\033[m!')
else:
    print(f'\nAh, eaí \033[1;33m{nome.title()}\033[m. Bem vindo, pessoa estranha.')