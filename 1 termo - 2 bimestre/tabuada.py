resp = 's'

while resp == 's':

    num = int(input('Digite a tabuada: '))

    while (num <= 0 or num > 10):
        print('Valor inválido, tente novamente.')
        num = int(input('Digite a tabuada: '))

    n = 1

    # while n <= 10:
    #     tabuada= num * n
    #     print('%d x %d = %d'%(num, n, tabuada))
    #     n += 1

    for n in range(1,11,1):
        tabuada = num * n
        print('%d x %d = %d' % (num, n, tabuada))

    resp = input('Deseja calcular outra tabuada? (s/n): ').lower()
    while (resp != 's' and resp != 'n'):
        print('Opção inválida, tente novamente.')
        resp = input('Deseja calcular outra tabuada? (s/n): ').lower()

    # resp = resp.lower()
    #upper (maiúsculo) - lower (minúsculo)

