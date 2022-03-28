def validationCNPJ(string):
    string= string.replace('.','').replace('/','').replace('-','')
    cnpjlist=[]
    cnpjoriginal=[]
    for i in string:
        i=int(i)
        cnpjlist.append(i)
        cnpjoriginal.append(i)
    cnpjlist.pop()
    cnpjlist.pop()

    validador1=[5,4,3,2,9,8,7,6,5,4,3,2]
    somacnpj1=sum([x*y for x,y in zip(cnpjlist,validador1)])
    formula1= 11-(somacnpj1 % 11)

    cnpjlist.append(formula1)
    validador2=[6,5,4,3,2,9,8,7,6,5,4,3,2]
    somacnpj2=sum([x*y for x,y in zip(cnpjlist,validador2)])
    formula2=11-(somacnpj2 % 11)
    cnpjlist.append(formula2)

    if cnpjlist==cnpjoriginal:
        return True
    else:
        return False


'''
cnpj='34.752.179/0001-55'
print(validationCNPJ(cnpj))'''