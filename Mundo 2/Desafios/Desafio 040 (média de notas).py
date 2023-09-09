m1 = float(input('Digite a primeira média: '))
m2 = float(input('Digite a segunda média: '))
média = (m1+m2)/2
if média < 5:
    print(f'\nREPROVADO (média de {média})')
elif média >= 5 and média <= 6.9:
    print(f'\nRECUPERAÇÃO (média de {média})')
else:
    print(f'\nAPROVADO (média de {média})')