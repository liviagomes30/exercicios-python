''' João foi jogar no “Cassino Bellagio em Las Vegas”,ele terá que converter o valor do dólar. Faça umprograma que irá receber como entrada a cotação dodólar, um valor em dólar e converta esse valor parareal. Mostre o resultado para o João. '''

cotacao = float(input('Digite a cotação do dólar: '))
dolar = float(input('Digite um valor em dólar para conversão: '))
real = dolar*cotacao
print('Valor de %.2f dólares em reais: %.2f'%(dolar,real))
