nome = (input('Digite aqui o nome completo: '))

print()

print(nome.upper())
print(nome.lower())

nospc = int(len(nome)) - int(nome.count(' '))

print(nospc)

fname = nome.split()

print(len(fname[1]))
