def fatorial(numero):
    if(numero < 1): # base da recursão
        return 1
    else:
        return numero * (fatorial(numero-1)) # chamada recursiva
