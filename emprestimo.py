''' Faça um programa que, ao entrar com o salário bruto eo valor da prestação, seja informado se o empréstimopode ou não ser concedido.
OBS: o valor da prestação não poderá ultrapassar 30%do salário.'''

salario = float(input('Digite o salário: '))
prest = float(input('Digite o valor da prestação: '))
if prest > salario*0.3:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')