nome = str(input('Digite o nome completo: '))

divnome = nome.strip().lower().title().split()

print()
print(f'O primeiro nome é: {divnome[1]}')
print(f'O último nome é: {divnome[-1]}')