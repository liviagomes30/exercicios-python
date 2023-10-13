# 3)	[E/S, comandos de decisão e listas] Jogo do Pedra – Papel – Tesoura, também chamado em algumas regiões do Brasil de jokempô é um jogo de mãos recreativo e simples para duas ou mais pessoas, que não requer equipamentos nem habilidade. A forma de jogar é a seguinte: os jogadores devem simultaneamente esticar a mão, na qual cada um formou um símbolo (que significa pedra, papel ou tesoura). Então, os jogadores comparam os símbolos para decidir quem ganhou, da seguinte forma: Pedra ganha da tesoura (amassando-a ou quebrando-a). Tesoura ganha do papel (cortando-o). Desenvolva um programa em Python em que você jogue com o computador, você escolhe um dos 3 símbolos e o computador sorteia aleatoriamente um dos 3 símbolos para ele, seu programa deverá processar e informar quem foi o ganhador da rodada.

import random

op = input('\nDeseja jogar Pedra, Papel ou Tesoura? (S/N):').upper()
while op == 'S':
    escolhaUsu = input('Digite pedra, papel ou tesoura: ').lower()

    if (escolhaUsu != 'pedra' and escolhaUsu != 'papel' and escolhaUsu != 'tesoura'):
        print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
        continue

    escolhaComp = random.choice(["pedra", "papel", "tesoura"])

    print("Você escolheu:", escolhaUsu)
    print("Computador escolheu:", escolhaComp)

    if escolhaUsu == escolhaComp:
        print("Empate")
    elif (escolhaUsu == 'pedra' and escolhaComp == 'tesoura') or (escolhaUsu == 'papel' and escolhaComp == 'pedra') or (escolhaUsu == 'tesoura' and escolhaComp == 'papel'):
        print("Você ganhou")
    else:
        print("Computador ganhou")

    op = input('Deseja jogar Pedra, Papel ou Tesoura? (S/N):').upper()
