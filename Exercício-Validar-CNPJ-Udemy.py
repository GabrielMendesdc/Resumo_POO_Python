def validadorCnpj(cnpj):
    antigo = cnpj
    lista1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    listasoma = []
    lista2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    predigitos = ''
    try:
        cnpj = str(cnpj)
        cnpj = cnpj.replace('.','').replace('/','').replace('-','')
    except:
        return "insira um cnpj valido"
    if len(cnpj) > 12:
        predigitos = cnpj[12:]
        cnpj = cnpj[:12]
    for i in range(len(cnpj)):
        listasoma.append(int(cnpj[i])*lista1[i])
    formulad1 = 11 - (sum(listasoma) % 11)
    if formulad1 > 9:
        formulad1 = 0
    listasoma = []
    cnpj = cnpj+str(formulad1)
    for i in range(len(cnpj)):
        listasoma.append(int(cnpj[i])*lista2[i])
    formulad2 = 11 - (sum(listasoma) % 11)
    if formulad2 > 9:
        formulad2 = 0
    cnpj = cnpj+str(formulad2)
    if predigitos:
        if predigitos == cnpj[12:]:
            return f'CNPJ {antigo} é válido'
    return cnpj
print(validadorCnpj('12.544.992/0001'))