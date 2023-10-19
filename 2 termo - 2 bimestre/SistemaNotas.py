# Livia Gomes de Souza
listaAlunos = []
aluno = {}

listaAlunos.append({'nome': 'pedro', 'notas':[7.5, 6.0,5.5]})
listaAlunos.append({'nome': 'livia', 'notas':[10, 7.0,8.5]})

print('\n### Menu ###')
print('1. Adicionar um aluno com suas notas.')
print('2. Atualizar as notas de um aluno existente.')
print('3. Calcular a média das notas de um aluno.')
print('4. Listar todos os alunos e suas notas.')
print('5. Encontrar o aluno com a maior média.')
print('6. Encontrar o aluno com a menor média.')
print('0. Finalizar programa.')
op = input('\nDigite a opção desejada:')

while op != '0':

    if op == '1':
        aluno = {} # para não sobrescrever os alunos
        aluno['nome'] = input('Digite o nome do aluno(a): ').strip().lower()
        while not aluno['nome'].isalpha() or not aluno['nome']: # verificando se é alfabético e se não é vazio
            print("Nome inválido. Tente novamente.")
            aluno['nome'] = input('Digite o nome do aluno(a): ').strip().lower()

        qtdeProvas = int(input('Digite a quantidade de provas realizadas: '))
        while qtdeProvas <= 0:
            print("Quantidade inválida. Tente novamente.")
            qtdeProvas = int(input('Digite a quantidade de provas realizadas: '))

        aluno['notas'] = []

        for i in range(0, qtdeProvas):
            nota = float(input('Digite a %dª nota: ' % int(i + 1)))
            while nota < 0 or nota > 10:
                print("Nota inválida. Deve ser um número entre 0 e 10. Tente novamente.")
                nota = float(input('Digite a %dª nota: ' % int(i + 1)))
            aluno['notas'].append(nota)

        listaAlunos.append(aluno)

    elif op == '2':
        if not listaAlunos:
            print("Não há alunos cadastrados.")
        else:
            nome = input("Digite o nome do aluno que deseja atualizar as notas: ").strip().lower()
            for aluno in listaAlunos:
                if aluno['nome'] == nome:
                    qtdeProvas = int(input('Digite a quantidade de provas realizadas: '))
                    while qtdeProvas <= 0:
                        print("Quantidade inválida. Tente novamente.")
                        qtdeProvas = int(input('Digite a quantidade de provas realizadas: '))

                    aluno['notas'] = []
                    for i in range(0, qtdeProvas):
                        nota = float(input('Digite a %dª nota: ' % int(i + 1)))
                        while nota < 0 or nota > 10:
                            print("Nota inválida. Deve ser um número entre 0 e 10. Tente novamente.")
                            nota = float(input('Digite a %dª nota: ' % int(i + 1)))
                        aluno['notas'].append(nota)

                    print("Notas atualizadas com sucesso!")

    elif op == '3':
        if not listaAlunos:
            print("Não há alunos cadastrados.")
        else:
            nome = input("Digite o nome do aluno que deseja calcular a média: ").strip().lower()
            for aluno in listaAlunos:
                if aluno['nome'] == nome:
                     mediaAluno = sum(aluno['notas'])/len(aluno['notas'])
                     print('A média do aluno é:',mediaAluno)
                else:
                    print("Aluno não encontrado.")

    elif op == '4':
        if not listaAlunos:
            print("Não há alunos cadastrados.")
        else:
            for aluno in listaAlunos:
                print('\nNome:',aluno['nome'].capitalize())
                print('Notas:',aluno['notas'])

    elif op == '5':
        if not listaAlunos:
            print("Não há alunos cadastrados.")
        else:
            maiorMedia = 0

            for aluno in listaAlunos:
                mediaAluno = sum(aluno['notas'])/len(aluno['notas'])

                if mediaAluno > maiorMedia:
                    maiorMedia = mediaAluno
                    alunoMaiorMedia = aluno

            if alunoMaiorMedia:
                print('Aluno(a) com a maior média:')
                print('Nome:',alunoMaiorMedia['nome'].capitalize())
                print('Notas:',alunoMaiorMedia['notas'])
                print('Média:', sum(alunoMaiorMedia['notas'])/len(alunoMaiorMedia['notas']))


    elif op == '6':
         if not listaAlunos:
             print("Não há alunos cadastrados.")
         else:
             menorMedia = 11

             for aluno in listaAlunos:
                 mediaAluno = sum(aluno['notas']) / len(aluno['notas'])

                 if mediaAluno < menorMedia:
                     menorMedia = mediaAluno
                     alunoMenorMedia = aluno

             if alunoMenorMedia:
                 print('Aluno(a) com a menor média:')
                 print('Nome:', alunoMenorMedia['nome'].capitalize())
                 print('Notas:', alunoMenorMedia['notas'])
                 print('Média:', sum(alunoMenorMedia['notas']) / len(alunoMenorMedia['notas']))
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')

    print('\n### Menu ###')
    print('1. Adicionar um aluno com suas notas.')
    print('2. Atualizar as notas de um aluno existente.')
    print('3. Calcular a média das notas de um aluno.')
    print('4. Listar todos os alunos e suas notas.')
    print('5. Encontrar o aluno com a maior média.')
    print('6. Encontrar o aluno com a menor média.')
    print('0. Finalizar programa.')
    op = input('\nDigite a opção desejada:')





