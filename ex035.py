a = float(input('Digite o primeiro lado do triangulo: '))
b = float(input('Digite o segundo lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))


if a < b+c and b < a+c and c < a+b:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos acima não podem formar um triangulo')

x = input('')