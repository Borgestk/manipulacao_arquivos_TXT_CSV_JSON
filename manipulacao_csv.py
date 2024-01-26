### importar o modulo csv
import csv



### criar um arquivo csv com as funcoes writer e writerow
with open('arquivos/nomes.csv','w+',newline="",encoding='utf-8') as fcsv:
    escreve = csv.writer(fcsv,delimiter=',')
    escreve.writerow(('nome',"sobrenome",'idade'))
    escreve.writerow(('João',"Manoel",'17'))
    escreve.writerow(('Gizele',"Souza",'34'))
    escreve.writerow(('Bruno',"Borges",'16'))



##ler o arquivo csv criado
with open('arquivos/nomes.csv','r') as fcsv:
    ler = csv.reader(fcsv)
    lista1 = list(ler)
    print(lista1)
    for c in lista1:
        print(c)


##transformar a saida em dicionario com o metodo desctreader
with open('arquivos/nomes.csv','r')as fcsv2:
    ler_dic = csv.DictReader(fcsv2)


#iterar os valores
    for d in ler_dic:
        print(d["nome"])

