novo_usuario = "SIM"

while novo_usuario == "SIM":
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    resposta = input("Suspeita de doença infectocontagiosa? ").upper()

    # PRIMEIRO PROBLEMA A SER RESOLVIDO
    while resposta != "SIM" and resposta != "Não":
        print("Digite SIM ou NÃO")
        resposta = input("Suspeita de doença infectocontagiosa? ").upper()

    if resposta == "SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif resposta == "NÃO":
        print("Encaminhe o paciente para sala BRANCA")

    # SEGUNDO PROBLEMA A SER RESOLVIDO
    if idade >= 65:
        print("Paciente COM prioridade")
    else:
        genero = input("Digite o gênero do paciente: ").upper()
        if genero == "FEMININO" and idade > 10:
            gravidez = input("A paciente está grávida? ").upper()
            if gravidez == "SIM":
                print("Paciente COM prioridade")
            else:
                print("Paciente SEM prioridade")
        else:
            print("Paciente SEM prioridade")

    novo_usuario = input("Deseja adicionar outro usuário? ").upper()
