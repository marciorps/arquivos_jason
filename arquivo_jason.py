#JSON - (javascript Object Notation)
import json

with open('usuarios1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)#converter um arquivo json para uma string
    print(data["nome"])

with open('usuarios2.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["permissões"][1])

with open('usuarios3.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuários"][0]["telefone"])
    print(data["usuários"][1]["admin"])

with open('usuarios4.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuários"][0]["plano"]["preco"])

with open('usuarios5.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data[0]["admin"])


# Imprimir o e-mail do usuário com id 2
# imprimir a city do usuário com id 1
# Imprimir o total do pedido do usuário com id 2

with open('desafio.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["user"][1]["email"])
    print(data["user"][0]["address"]["city"])
    print(data["user"][1]["orders"][0]["total"])