def minutos(horas, minutos):
    resposta = (horas * 60) + minutos
    return resposta

horas = int(input())
minutos_inicias = int(input())
print(minutos(horas, minutos_inicias))
