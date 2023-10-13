sim = 0
não = 0
indi = 0
nãoM = 0
simF = 0
cont = 0
sexo = input('Digite o sexo: (m/f ou outra letra para sair): ').lower()
while (sexo == 'f' or sexo == 'm'):
    idade = int(input('Digite a idade: '))
    resp = input('Está gostando do produto? (s = sim, n = não, i = indiferente): ').lower()
    if (resp == 's'):
        sim += 1
        if (sexo == 'f'):
            simF += 1
    elif (resp == 'n'):
        não += 1
        if (sexo == 'm'):
            nãoM += 1
    else:
        indi += 1
    cont += 1
    sexo = input('Digite o sexo: (m/f ou outra letra para sair): ').lower()

print('\n%d pessoas foram entrevistadas'%cont)
print('%d pessoas disseram sim e %d pessoas disseram não'%(sim,não))
print('Percentual de pessoas que disseram não: %.2f%%'%((não/cont)*100))
print('Quantidade de mulheres que disseram sim: %d'%simF)
print('Quantidade de homens que disseram não: %d'%nãoM)




