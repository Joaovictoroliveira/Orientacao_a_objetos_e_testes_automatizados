#!/usr/local/bin/python3

def log(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da funcao: {function.__name__}')
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator

@log
def soma(x, y):
    return x + y

@log
def subtracao(x, y):
    return x - y

if __name__ == '__main__':
    print(soma(5, 7))
