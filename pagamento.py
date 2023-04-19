''' Elabore um algoritmo que calcule o que deve ser pagopor um produto, considerando o preço normal de venda ea escolha da condição de pagamento. Utilize os códigosda tabela a seguir para informar qual a condição depagamento escolhida pelo Usuário e efetue o cálculoadequado. Depois de executado o cálculo, deve-seinformar ao Usuário o valor de venda, o valor dodesconto ou juros, e o valor total a ser pago.

Código    Condição de Pagamento
1         À vista em dinheiro ou cheque, recebe 10% dedesconto.
2         À vista no cartão de crédito, recebe 5% dedesconto.
3         Em 2 vezes, preço normal de venda sem juros.
4         Em 3 vezes, preço normal de venda mais jurosde 10%.  '''

preçoVenda = float(input('Digite o preço de venda: '))
print('1 - À vista em dinheiro ou cheque\n2 - À vista no cartão de crédito\n3 - Em 2 vezes\n4 - Em 3 vezes\n')
cod = int(input('Digite o código do pagamento desejado: '))
if cod == 1:
    reajuste = preçoVenda*0.1
    valor_pagar = preçoVenda - reajuste
elif cod == 2:
    reajuste = preçoVenda*0.05
    valor_pagar = preçoVenda - reajuste
elif cod == 3:
    reajuste = 0
    valor_pagar = preçoVenda
else:
    reajuste = preçoVenda*0.1
    valor_pagar = preçoVenda + reajuste

print('Valor de venda: %.2f'%preçoVenda)
print('Valor do reajuste (desconto ou juros): %.2f'%reajuste)
print('Total à pagar: %.2f'%valor_pagar)