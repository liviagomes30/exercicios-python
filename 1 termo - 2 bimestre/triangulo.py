'''Crie um programa que a partir de três valores A,
B, C, verifique se formam um triângulo, se
formam, classifique em eqüilátero, isósceles ou
escaleno.
Entrada: três lados de um suposto triângulo (A,
B, C).
Saída: não compõem triângulo, triângulo
eqüilátero, triângulo isósceles, triângulo
escaleno. '''

A = float(input('Digite o valor do lado A: '))
B = float(input('Digite o valor do lado B: '))
C = float(input('Digite o valor do lado C: '))

if A < B+C and B < A+C and C < A+B:
    if A == B and B == C:
        print('Triângulo equilátero.')
    elif A == B or B == C or A==C:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno.')
else:
    print('Os lados não formam um triângulo.')