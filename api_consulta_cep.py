import requests

print('consulta CEP')

cep_input = input('Digite um CEP para consulta: ')

if len(cep_input) != 8:
    print('Quantidade de digitos invalida!')
    exit()
    
request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

print (request.json())