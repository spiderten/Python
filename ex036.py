print('\033[34mVamos analizar sua situação para emprestimo...')

valorcasa = float(input('Digite o valor do imovel que você deseja comprar: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite em quantos anos você vai pagar essa casa: \033[m'))

mensal = valorcasa / (anos*12)

if mensal >= (salario*0.3):
    print('')
    print('\033[31mO emprestimo não foi aprovado pois o valor mensal de pagamento excedeu 30% do seu salario\033[m')
else:
    print('\033[32mSeu emprestimo foi aprovado!\033[m')