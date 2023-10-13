# Faça um programa que receba uma frase e mostre a quantidade de vogais da frase digitada. 

# OBS: O programa deverá contar vogais maiúsculas e minúsculas.


frase = input('Digite uma frase: ').lower()
vogais = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u')
print('Quantidade de vogais: ',vogais)