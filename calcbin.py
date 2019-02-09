
num = int(input('Digite um numero inteiro: '))
print('')
print('''Escolha uma das bases para conversão:

[ 1 ] -- Converter para Binario.
[ 2 ] -- Converter para Octal.
[ 3 ] -- Converter para Hexadecimal.''')
print('')
opção = int(input('Digite a opcao desejada: '))
print('')

if opção == 1:
    print('-> {} Convertido para binario e igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('-> {} Convertido para octal e igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('-> {} Convertido para Hexadecimal e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção nao encontrada. tente outra vez')
print('')

input("Pressione <enter> para continuar")
