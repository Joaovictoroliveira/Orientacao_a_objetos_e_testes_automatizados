class  PesquisaBinaria:

    def main(self):
        minha_lista = list(input('Digite os valores da lista: '))
        indice = int(input('Digite o valor que deseja ver o indice: '))
        return self.pesquisa_binaria(minha_lista, indice)

    def pesquisa_binaria(self, lista, item):
        baixo = 0
        alto = len(lista) - 1

        while baixo <= alto:
            meio = int((baixo + alto) / 2)
            chute = lista[meio]

            if(chute == item):
                return meio
            elif(chute > item):
                alto = meio - 1
            else:
                baixo = meio + 1
        return None
