n = int(input('Digite a velocidade do veiculo: '))


if n > 80:
    multa = ((n - 80) * 7)
    print('O veiculo foi multado por excesso de velocidade. O valor da multa é de: R$ {}'.format(multa))
else:
    print('O veiculo não tem multas')