def busca_binaria(lista, elemento, minimo=0, maximo=None):
    if(maximo == None):
        maximo = len(lista) - 1

    if(maximo < minimo):
        return False
    else:
        meio = minimo + (maximo - minimo) // 2

    if(lista[meio] > elemento):
        return busca_binaria(lista, elemento, minimo, meio-1)
    elif(lista[meio] < elemento):
        return busca_binaria(lista, elemento, meio+1, maximo)
    else:
        return meio
