matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# matriz = []
# m0 = []
# m1 = []
# m2 = []
# temp = []
# for c in range(0, 3):
#     if c == 0:
#         for c1 in range(0,3):
#             temp.append(int(input(f'Digite um valor para [0, {c1}]: ')))
#             m0.append(temp)
#             temp.clear()
#     if c == 1:
#         for c2 in range(0, 3):
#             temp.append(int(input(f'Digite um valor para [1, {c2}]: ')))
#             m1.append(temp)
#             temp.clear()
#     if c == 2:
#         for c3 in range(0, 3):
#             temp.append(int(input(f'Digite um valor para [2, {c3}]: ')))
#             m2.append(temp)
#             temp.clear()
# mt.append(m0[:])
# mt.append(m1[:])
# mt.append(m2[:])

# matriz = [[0, 1, 2], [3, 4, 5], [5, 7, 8]]

# print()
# for lista in mt:
#     for v in lista:
#         print(f'[{v:^5}]', end=' ')
#     print('\n')
# print()

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()