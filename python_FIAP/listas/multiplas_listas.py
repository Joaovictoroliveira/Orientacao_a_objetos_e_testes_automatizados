equipamentos = []
valores = []
numeros_seriais = []
departamentos = []

resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    numeros_seriais.append(int(input("Número serial: ")))
    departamentos.append(input("Departamento: "))

    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("\nEquipamento..: ", (indice + 1))
    print("Nome...........: ", equipamentos[indice])
    print("Valor..........: ", valores[indice])
    print("Serial.........: ", numeros_seriais[indice])
    print("Departamento...: ", departamentos[indice])

busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor..: ", valores[indice])
        print("Serial.: ", numeros_seriais[indice])

depreciado = input("\nDigite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos)):
    if depreciado in equipamentos[indice]:
        valores[indice] = round(valores[indice] - (valores[indice] * 0.1), 2)
        print("Novo valor..: ", valores[indice])

serial = int(input("\nDigite o número serial do produto danificado: "))
for indice in range(0, len(equipamentos)):
    if serial == numeros_seriais[indice]:
        print('O produto de número serial', numeros_seriais[indice], 'foi removido')
        del(equipamentos[indice])
        del(valores[indice])
        del(numeros_seriais[indice])
        del(departamentos[indice])
        break

for indice in range(0, len(equipamentos)):
    print("\nEquipamento..: ", (indice + 1))
    print("Nome...........: ", equipamentos[indice])
    print("Valor..........: ", valores[indice])
    print("Serial.........: ", numeros_seriais[indice])
    print("Departamento...: ", departamentos[indice])
