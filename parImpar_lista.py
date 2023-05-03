lista = []
par = []
impar = []
for i in range(8):
    num = int(input("Digite um Número: "))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('Lista com todos elementos: ',lista)
print('Lista com elementos pares: ',par)
print('Lista com elementos ímpares: ',impar)
