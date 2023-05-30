import random
from unidecode import unidecode
from termcolor import colored
des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |    
=========
''']

categorias = {
    "Animais": ["cachorro", "gato", "ayron", "elefante", "leão", "tigre", "girafa", "panda", "lobo", "coelho", "golfinho", "leopardo", "zebra", "hipopótamo", "rinoceronte", "macaco"],
    "Frutas": ["maçã", "banana", "laranja", "uva", "morango", "abacaxi", "pera", "melancia", "manga", "kiwi", "pêssego", "limão", "cereja", "amora", "abacate"],
    "Países": ["brasil", "canadá", "japão", "méxico", "austrália", "alemanha", "china", "egito", "grécia", "índia", "itália", "rússia", "espanha", "argentina", "frança"],
    "Veículos": ["carro", "moto", "avião", "bicicleta", "barco", "ônibus", "caminhão", "trem", "helicóptero", "trator", "navio", "jet ski", "van", "carroça", "foguete"],
    "Cores": ["azul", "vermelho", "amarelo", "verde", "roxo", "laranja", "rosa", "preto", "branco", "marrom", "cinza", "violeta", "dourado", "prateado", "turquesa"],
    "Profissões": ["médico", "professor", "engenheiro", "advogado", "artista", "piloto", "bombeiro", "policial", "atleta", "chef", "jornalista", "arquiteto", "cientista", "escritor", "dançarino"]
}
resp=1
print(colored("----------x-------------x----------",attrs=["dark"]))
print(colored('***Bem vindo ao jogo da Forca!***','cyan',attrs=["bold"]))
print(colored("----------x-------------x----------",attrs=["dark"]))

while resp==1:
    categoria_escolhida = input(
    "Escolha uma categoria (Animais, Frutas, Países, Veículos, Cores, Profissões): ")
    categoria_escolhida = categoria_escolhida.lower().capitalize()

    while categoria_escolhida not in categorias:
        print("Categoria inválida. Tente novamente.")
        categoria_escolhida = input(
        "Escolha uma categoria (Animais, Frutas, Países, Veículos, Cores, Profissões): ")
        categoria_escolhida = categoria_escolhida.lower().capitalize()

    palavras = categorias[categoria_escolhida]
    palavra = random.choice(palavras)
    palavra_sem_acentos = unidecode(palavra)
    letras_acertadas = []
    letras_erradas = []
    acertos = 0
    erros = 0

    while acertos < len(palavra) and erros != 7:
        mensagem = ''
        for letra in palavra:
            if unidecode(letra.lower()) in letras_acertadas:
                mensagem += f'{letra} '
            else:
                mensagem += '_ '
        print(des_forca[erros])
        print(mensagem)
        tentativa = input("\nEscolha uma letra para advinhar: ").lower().strip()
        cont = palavra_sem_acentos.count(unidecode(tentativa))
        if tentativa in letras_erradas+letras_acertadas:
            print(colored("Você já tentou essa letra","yellow"))
            continue  # interrompe execução do while e volta no início dele

        if unidecode(tentativa) in palavra_sem_acentos:
            print(colored("Você acertou a letra!","green"))
            letras_acertadas.append(tentativa)
            # palavrafinal.append(tentativa)
            acertos = acertos+cont  # letras repetidas
        else:
            print(colored("Você errou a letra!","red"))
            letras_erradas.append(tentativa)
            erros += 1
            if (erros != 7):
                print('Você ainda tem {} tentativa(s)'.format(7 - erros))

    if acertos == len(palavra):
         print(colored("----------x-------------x----------", attrs=["dark"]))
         print(colored("Você ganhou!", "green"))
         print(des_forca[erros])
         print(colored(palavra, "green"))
         print(colored("----------x-------------x----------", attrs=["dark"]))
    else:
         print(colored("----------x-------------x----------", attrs=["dark"]))
         print(colored("Você perdeu!", "red"))
         print('A palavra certa era : {}'.format(palavra))
         print(colored("----------x-------------x----------", attrs=["dark"]))
    resp = int(input("Deseja jogar novamente? 1-SIM ou 2-NÃO: "))
print("\n")
input("Pressione <enter> para encerrar!")