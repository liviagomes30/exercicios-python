resposta = []

print('Digite 1 para sim e 2 para não.')
resposta.append(int(input('Telefonou para a vítima? ')))
resposta.append(int(input('Esteve no local do crime? ')))
resposta.append(int(input('Mora perto da vítima? ')))
resposta.append(int(input('Devia para a vítima? ')))
resposta.append(int(input('Já trabalhou com a vítima? ')))
sim = resposta.count(1)
if sim == 2:
    print('Suspeita')
elif sim == 3 or sim == 4:
    print('Cúmplice')
elif sim == 5:
    print('Assassino')
else:
    print('Inocente')