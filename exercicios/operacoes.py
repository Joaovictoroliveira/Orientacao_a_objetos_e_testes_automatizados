def operacoes(operacao, numeros):
    num1 = float(numeros[0])
    num2 = float(numeros[1])

    if operacao == 'M':
        resultado = round(num1 * num2, 2)
    elif operacao == 'D':
        resultado = round(num1 / num2, 2)

    return resultado

operacao = input().upper()
numeros = input().split()
print(operacoes(operacao, numeros))
