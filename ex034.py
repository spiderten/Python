n = float(input('Digite o valor do seu salario: '))

if n > 1250.00:
    x = (n * 0.10) + n
    print('Seu salario com o novo aumento é: {}'.format(x))
else:
    x = (n * 0.15) + n
    print('Seu salario com o novo aumento é: {}'.format(x))
