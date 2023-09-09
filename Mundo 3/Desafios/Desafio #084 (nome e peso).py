'''pessoas = list()
dados = list()
maiores_pesos = list()
menores_pesos = list()
contagem = stop = peso_max = peso_min = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    contagem += 1
    stop = (str(input('Deseja continuar? [S/N] '))).strip().upper()
    if stop == 'N':
        break
# pessoas = [['Maria', 70],
#            ['Joao', 100],
#            ['Claudio', 85],
#            ['Hélio', 100],
#            ['Ana', 70],
#            ['Gustavo', 88]]
for c, p in enumerate(pessoas):
    if c == 0:
        peso_max += p[1]
        peso_min += p[1]
        maiores_pesos.append(p[:])
        menores_pesos.append(p[:])
    else:
        if p[1] >= peso_max:
            if p[1] > maiores_pesos[-1][1]:
                maiores_pesos.clear()
                maiores_pesos.append(p[:])
            else:
                maiores_pesos.append(p[:])
            peso_max = 0
            peso_max += p[1]
        if p[1] <= peso_min:
            if p[1] < menores_pesos[-1][1]:
                menores_pesos.clear()
                menores_pesos.append(p[:])
            else:
                menores_pesos.append(p[:])
            peso_min = 0
            peso_min = p[1]
if len(maiores_pesos) == 0:
    maiores_pesos.append(pessoas[0])
if len(menores_pesos) == 0:
    menores_pesos.append(pessoas[0])
print('-=' * 40)
print(f'Ao todo, você cadastrou {contagem} pessoas.')
print(f'O maior peso foi de {maiores_pesos[0][1]}Kg. Peso de ', end='')
for p in maiores_pesos:
    print(p[0], end='; ')
print(f'\nO menor peso foi de {menores_pesos[0][1]}Kg. Peso de ', end='')
for p in menores_pesos:
    print(p[0], end='; ')
print()'''

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de: ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {men}Kg.')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')