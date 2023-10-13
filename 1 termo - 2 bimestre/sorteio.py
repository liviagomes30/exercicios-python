import random

# print(random.random()) #Gera um valor aleatório entre 0 e 1
# print(10 * random.random()) #Gera número aleatório entre 1 e 10 (com decimais)
# print(random.uniform(4, 10)) #Valor decimal de 4 a 10
# print(random.randint(12, 55)) #Valor inteiro entre 12 e 55

nome = input('Digite seu nome: ')
print('Olá %s! Tente adivinhar o número entre 1 a 20'%nome)

tentativas = 0
num = random.randint(1, 20)

chute = 0

while tentativas < 6 and num != chute:
    chute = int(input('Digite o número pensado: '))

    if chute == num:
        print('\nParabéns %s, você acertou! O número é o %d.'%(nome, num))
    else:
        tentativas += 1
        if tentativas == 6:
            print('\nSinto muito, o número sorteado era o %d.' % num)
        else:
            print('\nValor incorreto, tente novamente.')












