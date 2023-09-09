n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
print()

if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

#ou

#maior = n1
#if n2>n1 and n2>n3:
    #maior = n2
#if n3>n1 and n3>n3:
    #maior = n3
#menor = n1
#if n2<n1 and n2<n3:
    #menor = n2
#if n3<n1 and n3<n2:
    #menor = n3

if (maior == n1 or menor == n1) and (menor == n3 or maior == n3):
    mediano = n2
if (maior == n2 or menor == n2) and (menor == n3 or maior == n3):
    mediano = n1
if (maior == n1 or menor == n1) and (menor == n2 or maior == n2):
    mediano = n3

print(f'O menor número é {menor} e o maior número é {maior}.')
print()
print(f'{menor}<{mediano}<{maior}')
