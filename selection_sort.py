def ordena(lista):           
    novaLista = []
    for i in range(len(lista)):
        menor= min(lista)
        novaLista.append(menor)
        lista.remove(menor)
    return novaLista
