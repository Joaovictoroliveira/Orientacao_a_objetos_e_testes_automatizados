resposta = "SIM"

while resposta == "SIM":
    nivel_acesso = input("Digite o nível de acesso: ").upper()
    if nivel_acesso == "ADM" or nivel_acesso == "USR":
       genero = input("Digite o seu gênero: ")
       if nivel_acesso == "ADM":
           if genero == "FEMININO":
               print("Olá administradora")
           else:
               print("Olá adminstrador")
       else:
           if genero == "FEMININO":
               print("Olá usuária")
           else:
               print("Olá usuário")
    elif nivel_acesso == "GUEST":
        print("Olá visitante")
    else:
        print("Olá desconhecido(a)")
    resposta = input("Digite SIM para continuat: ").upper()
