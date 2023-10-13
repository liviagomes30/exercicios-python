n=1
maior = 0
for n in range(1,7,1):
    idade = int(input('Digite a %da. idade: '%n))
    while (idade <= 0 or idade > 120):
        print('Idade inválida, digite novamente')
        idade = int(input('Digite a %da. idade: ' % n))
    if idade >= 18:
        maior += 1
print('%d pessoa(s) são maiores de idade'%maior)