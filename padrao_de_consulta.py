import re

string_teste = 'O gato é bonito'

padrao1 = input('Digite o padrao para consulta: ')


padrao = re.search(padrao1, string_teste)

if padrao:
    print(padrao.group())
else:
    print("Padrão não encontrado")