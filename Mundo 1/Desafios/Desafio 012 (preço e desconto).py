v = int(input('Digite um valor: '))

#inserir em <desc> o desconto (porcentagem)
desc = 5

cdesc = desc/100
vt = v-(v*cdesc)

print()
print(f'Valor com {desc}% de desconto: {vt}')