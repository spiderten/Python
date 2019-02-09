n = int(input('Digite um numero: '))

x = n % 2
if x == 1:
    print('O numero digitado é \033[34mimpar')
else:
    print('O numero digitado é \033[31mpar')