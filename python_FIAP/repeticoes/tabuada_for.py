numero = int(input("Digite um número para ver a sua tabuada: "))

print("******** Tabuada do número:", numero, "*********")
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
