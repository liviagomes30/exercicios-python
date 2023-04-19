while(1):
    print("Escolha a classificação de um animal:\n")
    print("1 - Mamífero\n")
    print("2 - Ave\n")
    print("3 - Réptil\n")
    print("4 - Sair\n")

    tipo = int(input('Digite a classificação: '))

    if tipo == 1:
        print("\nEscolha uma das opções abaixo:\n")
        print("1 - Quadrúpede\n")
        print("2 - Bípede\n")
        print("3 - Voador\n")
        print("4 - Aquático\n")
        mam = int(input('Opção desejada: \n'))

        if mam == 1:
            print("\nEscolha uma das opções abaixo:\n")
            print("1 - Carnívoro\n")
            print("2 - Herbívoro\n")
            tipoM = int(input('Opção desejada: \n'))

            if tipoM == 1:
                print("\nO animal escolhido é o leão!\n\n")
            elif tipoM == 2:
                print("\nO animal escolhido é o cavalo!\n\n")
            else:
                print("Opção inválida.\n\n")

        elif mam == 2:
            print("\nEscolha uma das opções abaixo:\n")
            print("1 - Onívoro\n")
            print("2 - Frutívoro\n")
            tipoM = int(input('Opção desejada: \n'))

            if tipoM == 1:
                print("\nO animal escolhido é o homem!\n\n")
            elif tipoM == 2:
                print("\nO animal escolhido é o macaco!\n\n")
            else:
                print("Opção inválida.\n\n")

        elif mam == 3:
            print("\nO animal escolhido é o morcego!\n\n")
        elif mam == 4:
            print("\nO animal escolhido é a baleia!\n\n")
        else:
            print("Opção inválida.\n\n")

    elif tipo == 2:
        print("\nEscolha uma das opções abaixo:\n")
        print("1 - Não Voadoras\n")
        print("2 - Nadadoras\n")
        print("3 - De Rapina\n")
        ave = int(input('Opção desejada: \n'))
        if ave == 1:
            print("1 - Tropical\n")
            print("2 - Polar\n")
            tipoA = int(input('Opção desejada: \n'))
            if tipoA == 1:
                print("\nO animal escolhido é o avestruz!\n\n")
            elif tipoA == 2:
                print("\nO animal escolhido é o pinguim!\n\n")
            else:
                print("Opção invalida.\n\n")
        elif ave == 2:
            print("\nO animal escolhido é o pato!\n\n")
        elif ave == 3:
            print("\nO animal escolhido é a águia!\n\n")
        else:
            print("Opção inválida.\n\n")

    elif tipo == 3:
        print("\nEscolha uma das opcoes abaixo:\n")
        print("1 - Com casco\n")
        print("2 - Carnívoro\n")
        print("3 - Sem patas\n")
        rep = int(input('Opção desejada: \n'))
        if rep == 1:
            print("\nO animal escolhido é a tartaruga!\n\n")
        elif rep == 2:
            print("\nO animal escolhido é o crocodilo!\n\n")
        elif rep == 3:
            print("\nO animal escolhido é a cobra!\n\n")
        else:
            print("Opção inválida.\n\n")

    elif tipo == 4:
        break;

    else:
        print("Opção inválida.\n\n")






