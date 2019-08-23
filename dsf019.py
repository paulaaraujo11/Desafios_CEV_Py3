from random import choice
print('=======Desafio 019=========\n')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunos_list = [n1, n2, n3, n4]
aluno_escolhido = choice(alunos_list)
print('O aluno escolhido é {}'.format(aluno_escolhido))
