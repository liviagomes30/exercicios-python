def maisde5(lista):
    print('----------------------------------------------')
    print('\nEstudantes com mais de 5 notas:\n')
    for aluno in lista:
        if len(aluno['notas']) > 5:
            print('Nome:',aluno['nome'].capitalize(),'\n')
    print('----------------------------------------------')
def media(lista):
    print('\n   ***  Média dos alunos  ***   \n')
    for aluno in lista:
        print('Nome:', aluno['nome'].capitalize())
        print('Média:',sum(aluno['notas'])/len(aluno['notas']),'\n')
    print('----------------------------------------------')

def maiorNota(lista):
    print('\n   ***  Maior nota ***   \n')
    for aluno in lista:
        maior = 0
        for nota in aluno['notas']:
            if nota > maior:
                maior = nota
        print('Nome:', aluno['nome'].capitalize())
        print('Maior nota:',maior,'\n')
    print('----------------------------------------------')