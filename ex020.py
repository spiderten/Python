import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

nomes = [n1, n2, n3, n4]

random.shuffle(nomes)

print('A sequencia de alunos para a apresentação dos trabalhos é: {}'.format(nomes))
x = input('')