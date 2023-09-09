def notas():
    dic={}
    notas=[]
    c=maior=menor=s=0
    dic['quant notas']=0
    while True:
        nota=float(input('Digite uma nota: '))
        if c==0:
            #maior=nota
            #menor=nota
            dic['maior']=nota
            dic['menor']=nota
        else:
            if nota > maior:
                #maior=nota
                dic['maior']=nota
            if nota < menor:
                #menor=nota
                dic['menor']=nota
        notas.append(nota)
        c+=1
        s+=nota
        dic['quant notas']=c
        escolha=str(input('Deseja digitar mais uma nota? [S/N]: '))
        if escolha in 'Nn':
            break
    #media=s/c
    dic['media']=s/c
    #if media>=6:
    if dic['media']>=6:
        #situacao='Boa'
        dic['situacao']='Boa'
    else:
        #situacao='Ruim'
        dic['situacao']='Ruim'
    #print(f'Quantidade de notas: {c}.', f'Maior nota: {maior}.', f'Menor nota: {menor}.', f'Média da turma: {media}.', f'Situação: {situacao}.')
    return(dic)
    #print(f'Notas digitadas: {notas}')


resp=notas()
print(resp)