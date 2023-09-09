from math import radians, sin, cos, tan

a = float(input('Digite o ângulo: '))

ac = radians(a)

sen = sin(ac)
cos = cos(ac)
tan = tan(ac)

print()
print(f'Valor do radiano: {ac:.4f}')
print()
print(f'Seno: {sen:.4f}')
print(f'Cosseno: {cos:.4f}')
print(f'Tangente: {tan:.4f}')