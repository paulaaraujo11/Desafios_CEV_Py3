from random import shuffle
print('=======Desafio 020=========\n')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
list_alunos = [n1, n2, n3, n4]
shuffle(list_alunos)
print('A ordem de apresentação será {}'.format(list_alunos))
