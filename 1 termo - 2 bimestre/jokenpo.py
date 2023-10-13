import random
opcoes = ('Pedra', 'Papel', 'Tesoura')
resp = input('Deseja jogar jokenpô? S ou N\n').upper()

while (resp == 'S'):
    PPT = input('Digite pedra, papel ou tesoura: ').lower().capitalize()
    pc = random.randint(0, 2)

    if pc == 0:
        if PPT == opcoes[0]:
            print('Empate\nEscolha do computador: {}'.format(opcoes[pc]))
        elif PPT == opcoes[2]:
            print(
                'Computador ganhou\nEscolha do computador: {}'.format(opcoes[pc]))
        elif PPT == opcoes[1]:
            print('Voce venceu\nEscolha do computador: {}'.format(opcoes[pc]))
        else:
            print('Opção inválida')

    if pc == 1:
        if PPT == opcoes[1]:
            print('Empate\nEscolha do computador: {}'.format(opcoes[pc]))
        elif PPT == opcoes[0]:
            print(
                'Computador ganhou\nEscolha do computador: {}'.format(opcoes[pc]))
        elif PPT == opcoes[2]:
            print('Voce venceu\nEscolha do computador: {}'.format(opcoes[pc]))
        else:
            print('Opção inválida')

    if pc == 2:
        if PPT == opcoes[2]:
            print('Empate\nEscolha do computador: {}'.format(opcoes[pc]))
        elif PPT == opcoes[1]:
            print(
                'Computador ganhou\nEscolha do computador: {}'.format(opcoes[pc]))
        elif PPT == opcoes[0]:
            print('Voce venceu\nEscolha do computador: {}'.format(opcoes[pc]))
        else:
            print('Opção inválida')

    resp = input('Deseja jogar jokenpô? S ou N\n').upper()
