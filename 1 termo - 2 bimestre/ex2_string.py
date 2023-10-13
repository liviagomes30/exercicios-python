# Faça um programa que leia uma string e um caractere e diga quantas vezes o caractere aparece na string.

string = input('Digite uma string: ').lower()
caractere = input('Digite um caractere a ser encontrado na string: ').lower()
ocorrencias = string.count(caractere)
print("Ocorrências do caractere",caractere,"na string: ",ocorrencias)
