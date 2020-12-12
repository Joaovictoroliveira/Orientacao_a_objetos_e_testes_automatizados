import random

def simula_dado():
    print("########## SIMULADOR DE DADO ###########")
    while True:
        jogar_dado = input("Você deseja jogar o dado? [S/N] ").upper()
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        if jogar_dado != 'S' and jogar_dado != 'N':
            print("Responda com S ou N")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        elif jogar_dado == 'N':
            break
        else:
            valor = random.randrange(1, 6)
            print(f'O número gerado foi {valor}')
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

simula_dado()
