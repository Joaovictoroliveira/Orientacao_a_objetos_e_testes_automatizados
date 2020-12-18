pesos = input().split()

p1 = int(pesos[0])
c1 = int(pesos[1])
p2 = int(pesos[2])
c2 = int(pesos[3])

if p1 * c1 == p2 * c2:
    print(0)
elif p1 * c1 > p2 * c2:
    print(-1)
elif p1 * c1 < p2 * c2:
    print(1)
