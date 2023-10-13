''' Os vilões do “Street Fighter” necessitam elaborar umesquema que troque o valor de 3 variáveis(golpes)para ganhar uma luta, vA, vB e vC, de forma que vAfique com o valor de vB, vB com o valor de vC e vCcom o valor de vA. Faça um ator receber os valorespara as variáveis vA, vB e vC que deverão serinformados como entrada e após a troca dos valores,mostre o resultado na tela. '''

vA = int(input('Digite o valor de vA: '))
vB = int(input('Digite o valor de vB: '))
vC = int(input('Digite o valor de vC: '))
aux = vA
vA = vB
vB = vC
vC = aux
print('vA: %d\nvB: %d\nvC: %d\n'%(vA,vB,vC))