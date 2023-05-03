gabarito = []
respostas = []
cont = 0
nome = input('Digite o nome: ')
for i in range(5):
    print('Digite o gabarito da {}a. questão: '.format(i+1))
    gabarito.append(input(''))
    print('Digite a resposta do(a) aluno(a) {} na {}a. questão: '.format(nome,i+1))
    respostas.append(input(''))
    if (gabarito[i] == respostas[i]):
        cont += 1

print('Pontuação: ',cont)
