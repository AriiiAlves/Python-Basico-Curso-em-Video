# from time import sleep
#
# def contador(i, f, p):
#     """<i>: Início da contagem
#     <f>: Fim da contagem
#     <p>: Passo a passo da contagem"""
#     f += 1
#     for c in range(i, f, p):
#         print(c, end=' ')
#         sleep(0.5)
#     print('FIM')
#
# help(contador)

# def somar(a=0, b=0, c=0):
#     s=a+b+c
#     return(s)
#
#
# resultado = somar(1, 2, 3)
# r2 = somar(1, 2)
# r3 = somar(1)
# print(resultado, r2, r3)


# def funcao():
#     global n1
#     n1=4
#     print(n1)
#
#
# n1=2
# funcao()
# print(n1)

def par(n=0):
    if n%2==0:
        return True
    else:
        return False


num=int(input('Digite um número: '))
if par(num):
    print('Par')
else:
    print('Ímpar')
