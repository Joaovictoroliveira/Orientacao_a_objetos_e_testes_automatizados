bandejas = int(input())
copos_quebrados = 0

for i in range(bandejas):
    bandeja = input().split()

    latas = int(bandeja[0])
    copos = int(bandeja[1])

    if copos < latas:
        copos_quebrados += copos
    
print(copos_quebrados)
