import random
n = int(input('Digite um numero de 0 a 5: '))

n1 = random.randint(0, 5)

if n == n1:
    print('Você venceu o jogo.')
else:
    print('Você perdeu o jogo.')

print('O numero escolhido pelo sistema foi: {}'.format(n1))