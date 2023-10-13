''' Faça um programa que leia o preço da mercadoria e o percentual de desconto.
- Calcule o valor do desconto;
- Calcule o valor a pagar;
- Imprima “Desconto de XX em uma mercadoria de XX”;
- Imprima o valor do desconto;
- Imprima o valor a pagar. '''

valor = float(input('Digite o valor da mercadoria: '))
percent = int(input('Digite o percentual de desconto: '))
print('Desconto de %.2f%% em uma mercadoria de %.2f'%(percent, valor))
percent = percent/100
desconto = valor*percent
valorFinal = valor - desconto
print('Desconto: %.2f'%desconto)
print('Valor a pagar: %.2f'%valorFinal)
