with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
    #for linha in conteudo:
    #    print(linha)

print("Tipo de dado da variável", type(conteudo))
print("Conteúdo do arquivo: ", conteudo)

