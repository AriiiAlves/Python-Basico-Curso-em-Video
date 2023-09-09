s = ''
a = 'incorreto'
sc = ''
while a == 'incorreto':
    if s == '':
        s = str(input('Digite seu sexo [M/F]: '))
    if s != '':
        if s.strip().lower() == 'm' or s.strip().lower() == 'f':
            a = 'correto'
        else:
            s = str(input('Valor incorreto, digite seu sexo novamente [M/F]: '))
            a = 'incorreto'
if s.strip().lower() == 'm':
    sc = 'Masculino'
if s.strip().lower() == 'f':
    sc = 'Feminino'
print(f'\nSeu sexo: {sc}')
