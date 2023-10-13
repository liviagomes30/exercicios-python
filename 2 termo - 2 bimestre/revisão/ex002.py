# 2)	 [E/S, comandos de decisão e repetição] Jogo da Adivinhação. Desenvolva um programa em Python que simule um jogo de adivinhação. Primeiramente, o programa deverá sortear um número entre 0 e 100. Após o sorteio, inicia-se o jogo e o jogador deverá tentar adivinhar o número sorteado. A cada tentativa, o jogo deverá informar se o “chute” do jogador foi maior ou menor do que o número a ser adivinhado. O jogo termina após vinte tentativas erradas ou quando o jogador acertar o número sorteado e, nesse caso, informe a quantidades de tentativas que foram necessárias. Após o término do jogo o jogador deverá decidir se deseja ou não iniciar um novo jogo.

from random import randint

novo_jogo = input('Jogo de adivinhação. Deseja começar? (sim/não): ').lower()
while novo_jogo == 'sim':
    numRandom = randint(0, 100)
    tentativas = 0

    while tentativas < 20:
        chute = int(input('\nDigite um número entre 0 e 100:'))
        tentativas += 1

        if chute > numRandom:
            print('Maior que o número escolhido')
        elif chute < numRandom:
            print('Menor que o número escolhido')
        else:
            print('\nParabéns, você acertou!')
            print('Número de tentativas =', tentativas)
            break

    if tentativas == 20:
        print('Suas 20 tentativas acabaram. O número era', numRandom)

    novo_jogo = input('\nDeseja jogar novamente? (sim/não): ').lower()
