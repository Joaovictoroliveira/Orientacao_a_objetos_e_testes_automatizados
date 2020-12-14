def binario_em_decimal():
    numero = input("Digite um número para converte-lo em decimal: ")
    decimal = int(numero, 2)
    print(decimal)

def decimal_em_binario():
    binario = ''
    numero = int(input("Digite um número para converte-lo em binario: "))

    while numero > 0:
        binario = binario + str(numero % 2)
        numero = (numero // 2)
    print(binario[::-1])

def main():
    resp = 'S'

    while resp == 'S':
        print("******************** Conversor de Números ********************")
        converter = int(input("digite 1 para converter um número decimal em número binário \nDigite 2 para converter um número binário em número decimal: "))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        if converter != 1 and converter != 2:
            while converter != 1 and converter != 2:
                print("Responda de acordo com o que foi pedido")
                converter = int(input("digite 1 para converter um número decimal em número binário \nDigite 2 para converter um número binário em número decimal: "))
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        if converter == 1:
            decimal_em_binario()
        elif converter == 2:
            binario_em_decimal()

        resp = input("Deseja continuar [S/N]? ").upper()

main()
