
## vamos abrir um arquivo TXT
arq1 = open('arquivos/arquivo.txt','r')


#windowns \ #linux /


### ler o arquivo TXT
print(arq1.read())


##voltar o cursor ao inicio 
arq1.seek(0,0)

print(arq1.read())


##fechar o arquivo
arq1.close()


## usar um arquivo em modo gravacao 
arq2 = open('arquivos/arquivo.txt','w+')


##gravar 
arq2.write("tem novo conteudo\n")
arq2.write("gravei outra linha\n")
arq2.seek(0,0)
print(arq2.read())


#fechar arquivo
arq2.close()


##abrir uma nova manipulacao de alteracao de arquivos 
arq3 = open('arquivos/arquivos.txt','a+')
arq3.write("novo conteudo sem apagar o antigo\n")
arq3.seek(0,0)
print(arq3.read())
arq3.close()

###gerenciador de contexto de arquivos

with open("arquivos/arquivo1.txt","w+") as f:
    f.write('primeira linha\n')
    f.write('segunda linha\n')
    f.seek(0,0)
    grava = str(f.read())
    f.seek(0,0)
    print(f.read())

## gravar informacoes em um 2 arquivo

with open('arquivos/arquivo2.txt','w+') as f2:
    f2.write(grava)
    f2.seek(0,0)
    print(f2.read())

