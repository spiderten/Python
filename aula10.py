tempo = float(input('Quanto tempo tem seu carro: '))

if tempo <= 3:
    print('Carro novo')
elif tempo >= 3.1 and tempo <= 6:
    print('Seu carro tem um tempo normal de uso')

else:
    print('Carro velho')
