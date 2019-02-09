n = int(input('Digite a distancia da sua viagem em km: '))

if n <= 200:
    x = n * 0.50
    print('O valor de sua viagem é R${}'.format(x))
else:
    x = n * 0.45
    print('O valor de sua viagem é R${}'.format(x))