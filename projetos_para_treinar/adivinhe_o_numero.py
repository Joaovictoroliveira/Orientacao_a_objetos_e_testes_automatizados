import random

def chute_um_numero():
    print("\n#############################################################\n")
    print("Estou pensando em um número entre 1 e 10, consegue adivinhar?")
    print("\n#############################################################\n")

    numero = random.randint(1, 10)

    while True:
        try:
            chute = int(input("Chute um número: "))
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        except:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Digite um número entre 1 e 10")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            continue

        if chute > numero:
            print("O número digitado é maior que o número que estou pensando...")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        elif chute < numero:
            print("O número digitado é menor que o número que estou pensando...")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        elif chute == numero:

            print("Parábens! Você adivinhou o número que eu estava pensando!!")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            break

chute_um_numero()
