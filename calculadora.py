''' Faça um programa que tenha como entrada 2 números, em seguida mostre um texto/menu para escolher a operação Desejada: + - * / '''


print("Selecione a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")
print("5 - Raiz quadrada")
print("6 - Potenciação")

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opcao = int(input("Digite sua opção (1/2/3/4/5/6): "))

if opcao == 1:
    resultado = num1 + num2
    print("Resultado: ", resultado)
elif opcao == 2:
    resultado = num1 - num2
    print("Resultado: ", resultado)
elif opcao == 3:
    resultado = num1 / num2
    print("Resultado: ", resultado)
elif opcao == 4:
    resultado = num1 * num2
    print("Resultado: ", resultado)
elif opcao == 5:
    resultado1 = num1 ** (1/2)
    resultado2 = num2 ** (1/2)
    print("Raiz quadrada do primeiro número: ", resultado1)
    print("Raiz quadrada do segundo número: ", resultado2)
elif opcao == 6:
    resultado = num1 ** num2
    print("Resultado: ", resultado)
else:
    print("Opção inválida!")
