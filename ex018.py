import math
n1 = float(input('Digite o valor de um angulo: '))

sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tg = math.tan(math.radians(n1))

print('O angulo digitado foi: {}\nO seno do angulo digitado é: {:.2f}\nO cosseno do angulo digitado é: {:.2f}\nA tangente do angulo digitado é: {:.2f}'.format(n1, sen, cos, tg))
