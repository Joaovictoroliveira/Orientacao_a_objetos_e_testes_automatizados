def area_circunferencia(raio):
    pi = 3.1416
    area = pi * pow(raio, 2)

    return round(area, 2)

raio = int(input())
print(area_circunferencia(raio))
