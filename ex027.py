nome = str(input('Digite seu nome completo: ')).strip()

n = nome.split()
print('O nome digitado foi "{}"'.format(nome))
print('O seu primeiro nome é: {}'.format(n[0]))
print('O seu ultimo nome é: {}'.format(n[len(n)-1]))
