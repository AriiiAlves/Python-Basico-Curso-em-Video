def area(a, b):
    #return(a*b)
    r = a*b
    print(f'A área de um terreno {a}m x {b}m é de {r}m.')
def linha(x, n):
    print('-'*n)
    print(x.center(n))
    print('-'*n)


linha('Controle de terrenos', 50)
area(2, 3)
area(5, 7)
area(8, 13)