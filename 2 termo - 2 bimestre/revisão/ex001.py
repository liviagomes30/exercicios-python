# 1)	[Strings] Palíndromos - Implemente um algoritmo em Python que verifica se uma frase é palíndroma (a mesma sequência de caracteres, se lida normalmente ou de trás para a frente: Por exemplo, as frases "roma me tem amor" e "socorram me subi no onibus em marrocos" são palíndromos).

frase = input('Digite uma frase:').replace(" ", "").lower()
fraseReversa = frase[::-1]


if frase == fraseReversa:
    print('É palíndromo')
else:
    print('Não é palíndromo')
