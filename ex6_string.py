# Implemente um algoritmo em Python que verificase uma palavra é palíndroma.

string = input('Digite uma palavra para verificação: ').lower()
reverso = string[::-1]
if (string == reverso):
    print('É palíndroma')
else:
    print('Não é palíndroma')