# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a+b
#     print(f'A soma A + B = {s}')
#     print('-'*18)
#
#
# # Programa Principal
# soma(b=4, a=5)
# soma(4, 5)
# soma(7, 2)

# def contador(*num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números')
#
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
#
#
# valores = [7, 2, 5, 0, 4]
# dobra(valores)
# print(valores)
# #nota: isso não é um desempacotamento.

#desempacotamento:
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)

