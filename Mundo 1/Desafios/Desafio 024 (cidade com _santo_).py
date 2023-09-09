cid = (input('Digite o nome de uma cidade: '))

#fcid = cid.strip().lower().count('santo', 0, 5)

#ou (resolução do guanabara)

#cid = str(input('Em que cidade você nasceu?')).strip()
#print(cid[:5].upper () == 'SANTO')

fcid = cid.lower().strip()

print('O nome da cidade começa com "Santo": ', 'santo' in fcid[:5])