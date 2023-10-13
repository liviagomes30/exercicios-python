# Faça um programa que receba o primeiro nome deuma pessoa e imprima-o na vertical.

nome = input('Digite o primeiro nome: ')

print('\nVertical:')
for i in range(len(nome)):
    print(nome[i])

# Modifique o programa anterior de forma amostrar o mesmo nome em formato escada.

print('\nCascata:')
for i in range(len(nome)):
    print(nome[:i+1])