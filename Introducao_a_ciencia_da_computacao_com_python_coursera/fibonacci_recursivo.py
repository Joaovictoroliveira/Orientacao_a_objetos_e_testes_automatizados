def fibonacci(numero):
    if(numero < 2): # base da recursão
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2) # chamada recursiva
