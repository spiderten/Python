import random
# formatação de cores
# \033[1;36;44m

# criar uma sequencia de cores

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho' :'\033[31m'}

print('{}a cor é{}!'.format(cores['azul'],cores['limpa'] ))

