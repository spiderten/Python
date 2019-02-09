a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
# verificando o menor
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c


# verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor numero digitado foi: {}'.format(menor))
print('O maior numero digitado foi: {}'.format(maior))
