# lista = []
# numeros = 0
# for c in range(0, 5):
#     n = int(input('Digite um valor numérico: '))
#     lista += [n]
# lista_copia = lista[:]
# lista[4] = max(lista_copia)
# lista[0] = min(lista_copia)
# lista_copia.remove(lista[0])
# lista_copia.remove(lista[4])
# lista[3] = max(lista_copia)
# lista[1] = min(lista_copia)
# lista_copia.remove(lista[1])
# lista_copia.remove(lista[3])
# lista[2] = lista_copia[0]
# print('\nLista: ', end='')
# for contagem, numero in enumerate(lista):
#     if contagem != 4:
#         print(numero, end=', ')
#     else:
#         print(numero)

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    # se for maior que o último número, vai para o final da lista
    if c == 0 or n > lista[-1]:
        lista.append(n)
    # senão...
    else:
        posição = 0
        # aqui, o while rodará a mesma quantidade de vezes
        # que o tamanho da lista. Ele vai inserindo o número
        # (ocupando a posição do outro se o número a ser adicionado
        # for igual ou menor ao que está nessa posição, adicionando
        # em ordem crescente cada número, e nunca substituindo os
        # números, apenas inserindo na posição, mudando a ordem dos
        # índices à frente.
        while posição < len(lista):
            if n <= lista[posição]:
                lista.insert(posição, n)
                break
            posição += 1
print(lista)
