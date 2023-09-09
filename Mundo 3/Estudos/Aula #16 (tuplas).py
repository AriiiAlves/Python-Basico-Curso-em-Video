lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
'''print(lanche[0:2])
print('-' * 10)
for c in lanche:
    print(c)
    print('-' * 10)'''

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')'''

#outro modo de fazer a mesma coisa:

'''for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Comi pra caramba!')'''

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

print(sorted(lanche))
print('Comi pra caramba!')


