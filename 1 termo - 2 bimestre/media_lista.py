lista = []
for i in range(4):
    print('Digite a {}a. nota: '.format(i+1))
    lista.append(float(input()))
media = sum(lista)/4
print('Notas: ',lista)
print('Média: ',media)
if media >= 7:
    print('Aprovado.')
else:
    print('Reprovado.')
