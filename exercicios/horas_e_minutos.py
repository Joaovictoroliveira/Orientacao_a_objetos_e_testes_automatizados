def horas_e_minutos(M):
    horas = M // 60
    minutos = M % 60

    return '{}\n{}'.format(horas, minutos)

M = int(input())
print(horas_e_minutos(M))
