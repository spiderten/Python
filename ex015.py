km = float(input('Informe a quantidade de Km percorridos com o veiculo alugado: '))
dias = int(input('Informe a quantidade de dias alugadas: '))
final = float((dias * 60) + (km * 0.15))

print('A valor total do aluguel do veiculo é de: {:.2f}'.format(final))