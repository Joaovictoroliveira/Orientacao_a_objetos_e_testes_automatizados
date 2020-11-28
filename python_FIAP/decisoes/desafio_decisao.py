nivel_acesso = input("Digite o nível de acesso: ").upper()
genero = input("Digite o gênero: ").upper()

if nivel_acesso == "ADM":
    if genero == "FEMININO":
        print("Olá administradora")
    elif genero == "MASCULINO":
        print("Olá administrador")
elif nivel_acesso == "USR":
    if genero == "FEMININO":
        print("Olá usuária")
    elif genero == "MASCULINO":
        print("Olá usuário")
elif nivel_acesso == "GUEST":
    print("Olá visitante")
else:
    print("Olá descinhecido(a)")
