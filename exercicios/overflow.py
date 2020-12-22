def overflow(N, lista):
    P = int(lista[0])
    Q = int(lista[2])
    caractere = lista[1]

    if caractere == '+':
        operacao = P + Q
    elif caractere == '*':
        operacao = P * Q

    if operacao <= N:
        return 'OK'
    return 'OVERFLOW'

N = int(input())
lista = input().split()
print(overflow(N, lista))
