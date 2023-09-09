from math import hypot

input('>Digite os valores em metros (m)!<')

print()

cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjascente: '))

#hip = math.sqrt(cat1**2+cat2**2)

hip = hypot(cat1, cat2)

print(f'O valor da hipotenusa é {hip:.2f} m')
