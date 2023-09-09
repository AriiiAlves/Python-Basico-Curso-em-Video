frase = str(input('Digite uma frase: '))

ffrase = frase.strip().lower()

print()
print(f'A letra "A" aparece {ffrase.count("a")} vezes')
print(f'A letra "A" aparece pela primeira vez na posição {ffrase.find("a")}')
print(f'A letra "A" aparece pela última vez na posição {ffrase.rfind("a")}')