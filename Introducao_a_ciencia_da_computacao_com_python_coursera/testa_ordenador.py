import bubblesort
import pytest
import conta_tempo

class TestaOrdenador:
    @pytest.fixture
    def o(self):
        return bubblesort.Ordenador()

    @pytest.fixture
    def lista_quase_ordenada(self):
        c = conta_tempo.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def lista_aleatoria(self):
        c = conta_tempo.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if (l[i] > l[i+1]):
                return False
        return True

    def testa_bolha_curta_aleatoria(self, o, lista_aleatoria):
        o.bolha_curta(lista_aleatoria)
        assert self.esta_ordenada(lista_aleatoria)

    def testa_selecao_direta(self, o, lista_aleatoria):
        o.selecao_direta(lista_aleatoria)
        assert self.esta_ordenada(lista_aleatoria)

    def testa_bolha_curta_quase(self, o, lista_quase_ordenada):
        o.bolha_curta(lista_quase_ordenada)
        assert self.esta_ordenada(lista_quase_ordenada)

    def testa_selecao_quase(self, o, lista_quase_ordenada):
        o.selecao_direta(lista_quase_ordenada)
        assert self.esta_ordenada(lista_quase_ordenada)
