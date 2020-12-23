def sort_by_lenght(lista):
    if len(lista) == 0:
        return []
    else:
        nova_lista = []
        menor = lista[0]

        while True:
            for i in lista:
                if len(menor) < len(i) and menor not in nova_lista:
                    nova_lista.append(menor)
                    lista.remove(lista[0])
                    menor = lista[0]
                elif len(i) < len(menor):
                    menor = i
                    nova_lista.append(menor)
                    lista.remove(i)
                    menor = lista[0]
                else:
                    if len(lista) == 1:
                        nova_lista.append(i)
                        lista.remove(i)
                            
            if len(lista) == 0:
                break

        return nova_lista

lista = []
print(sort_by_lenght(lista))
