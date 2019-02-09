nome = input('Digite o seu nome completo: ').strip()
print('Analisando seu nome...')

print('Seu nome completo em maiusculo é: {}'.format(nome.upper()))
print('Seu nome completo em minusculo é: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
