''' Construa um algoritmo que receba como entrada os seguintes dados:
         peso de uma pessoa
         altura em metros
Em seguida calcule o “IMC” através da seguinte fórmula: IMC = PESO / ALTURA²
Mostre sua condição de acordo com os itens abaixo:
         Abaixo de 18,5 - Abaixo do peso
         Entre 18,5 e 25 - Peso normal
         Entre 25 e 30 - Acima do peso
         Acima de 30 - Obeso '''

peso = float((input('Digite o peso em kg: ')))
altura = float(input('Digite a altura em m: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso normal')
elif imc > 25 and imc <= 30:
    print('Acima do peso')
else:
    print('Obeso')