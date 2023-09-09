frase = 'Curso em Vídeo Python'

print(frase)
print(frase[9])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print()

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print('Curso' in frase)

print()

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

print()

print(frase.split())

frase_split = frase.split()

print()

print('-'.join(frase_split))

print()

print(frase.lower().count('vídeo')) #conta a quantidade de 'vídeo' minúsculos na variável após ela ser colocada toda em minúsculas

#a variável é imutável. não pode ser alterada, apenas usada sua modificação. A menos que seja assim:

#frase = 'Curso em Vídeo Python'
#frase = frase.replace('Python', 'Android')
#print(frase)