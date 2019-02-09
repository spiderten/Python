frase = str(input('Digite uma frase: ')).strip().upper()

print('A frase digitada foi: {}'.format(frase))
print('A letra "A" aparece "{}" vezes na frase'.format(frase.count('A')))
print('A primeira ver que a letra "A" aparece é "{}"'.format(frase.find('A')+1))
print('A ultima ver que a letra "A" aparece é "{}"'.format(frase.rfind('A')+1))
