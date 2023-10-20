from biblioteca.modulos import *

arq=open('notas_estudantes.dat', 'a+') #leitura e escrita

#Usando o arquivo texto notas_estudantes.dat escreva uma função que:

# a) imprime o nome dos estudantes que têm mais de cinco notas;

arq.seek(0,0) #voltando ao inicio do arquivo

listaAlunos = []

# Quando você usa a função open para abrir um arquivo em Python no modo de leitura ("r"), por padrão, ele lê o arquivo linha por linha.
for linha in arq:
    dados = linha.split() # divide a linha em palavras

    # O primeiro elemento é o nome do aluno
    nome = dados[0]
    notas = []
    for nota in dados[1:]:
        notas.append(int(nota))

    aluno = {}
    aluno = {'nome':nome, 'notas':notas}
    listaAlunos.append(aluno)

maisde5(listaAlunos)
media(listaAlunos)
maiorNota(listaAlunos)

arq.close()