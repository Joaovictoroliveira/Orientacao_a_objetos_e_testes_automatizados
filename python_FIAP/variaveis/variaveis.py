nome = input("Digite um funcionario: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a quantidade de funcionarios: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: R$" + str(mediaMensalidade))

print("================= Verifique os tipos de dados abaixo ===============")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [empresa] é: ", type(empresa))
print("O tipo de dado da variável [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variável [mediaMensalidade] é: ", type(mediaMensalidade))
