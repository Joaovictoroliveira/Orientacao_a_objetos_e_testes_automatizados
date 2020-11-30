def preencherInventario(lista):
    resposta = "S"

    while resposta == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Número Serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resposta = input("Digite \"S\" para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])

def localizarPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")

    for elemento in lista:
        if busca == lista[elemento]:
            print("Valor: ", elemento[1])
            print("Serial: ", elemento[2])

def depreciarPorNome(lista, porcentagem):
    depreciacao = input("\nDigite o nome do equipamento que sera depreciado: ")

    for elemento in lista:
        if depreciacao == lista[elemento]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] - (elemento[1] * porcentagem)
            print("Novo valor: ", elemento[1])

def excluirPorSerial(lista):
    serial = input("\nDigite o serial do equipamento que será excluido: ")

    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
    return "Itens excluídos."

def resumirValores(lista):
    valores = []

    for elemento in lista:
        valores.append(elemento[1])

    if len(valores) > 0:
        print("Maior valor: ", max(valores))
        print("Menor valor: ", min(valores))
        print("Total dos valores: ", sum(valores))
