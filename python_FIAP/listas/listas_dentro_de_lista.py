inventario = []
resposta = 'S'

while resposta == 'S':
    equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Número Serial: ")),
                   input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print("Nome..........: ", elemento[0])
    print("Valor.........: ", elemento[1])
    print("Serial........: ", elemento[2])
    print("Departamento..: ", elemento[3])

busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.: ", elemento[2])

depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

serial = int(input("\nDigite o serial do equipamento que será excluído: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print("Nome..........: ", elemento[0])
    print("Valor.........: ", elemento[1])
    print("Serial........: ", elemento[2])
    print("Departamento..: ", elemento[3])

valores = []
for elemento in inventario:
    valores.append(elemento[1])

if len(valores) > 0:
    # max() -> retorna o maior valor numérico dentre os elementos da lista
    print("O equipamento mais caro custa: ", max(valores))

    # min() -> retorna o menor valor numérico dentre os elementos da lista
    print("O equipamento mais barato custa: ", min(valores))

    # sum() -> retorna o total entre os valores que estão na lista
    print("O total de equipamento é de: ", sum(valores))
