# Javascript Object notation
# ele e estruturado por chaves e valores (dicionario)

#json e usado para troca de informacoes entre sistemas backends
#e o formato utilizado pelas APIs
#graphql as APIs REST

## capturar uma informacao da internet ##

import urllib.request
import json

url = 'http://api.open-notify.org/astros.json'

##capturar essas informacoes em dados JSON

pega_json = urllib.request.urlopen(url).read().decode()

## converter esses valores em dicionarios para manipulacao 

dic_json = json.loads(pega_json)

##iterar os valores do dicionarios

for c in dic_json.values():
    print(c)

print(dic_json)

for p in dic_json['people']:
    print(p['name'],p['craft'])

##criar um arquivo json com os valores extraidos

with open('arquivos/nomes.json','w+')as f:
    json.dump(dic_json,f,indent=4)