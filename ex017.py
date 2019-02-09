import math
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))

x = ((math.pow(n1, 2) + (math.pow(n2, 2)) ))
x2 = math.sqrt(x)

print('O comprimento da hipotenusa é : {:.2f}'.format(x2))