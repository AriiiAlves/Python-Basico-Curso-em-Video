fcount = int(input('Fim da contagem: '))

print(f'\nNúmeros pares entre 0 e {fcount}:\n')
n = 0
for c in range(0, fcount):
    nf = n + 1
    nfres = str(nf)
    nfint = int(nfres)
    nfop = (nfres[-1:])
    #print(nfop)
    nfb = int(nfop)
    if nfint > 1 and nfint < fcount and (nfb == 0 or nfb == 2 or nfb == 4 or nfb == 6 or nfb == 8):
        print(nf)
    n = nf
print('\nFIM')