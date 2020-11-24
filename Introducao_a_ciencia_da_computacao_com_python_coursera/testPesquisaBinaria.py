import pesquisa_binaria
import pytest

class TestPesquisaBinaria:

    @pytest.fixture
    def pb(self):
        return pesquisa_binaria.PesquisaBinaria()

    def teste_1(self, pb):
        assert pb.pesquisa_binaria([1,3,5,7,9,11,13,15,17,19,21,23], 3) == 1

    def teste_2(self, pb):
        assert pb.pesquisa_binaria([1,3,5,7,9,11,13,15,17,19,21,23], 13) == 6

    def teste_3(self, pb):
        assert pb.pesquisa_binaria([1,3,5,7,9,11,13,15,17,19,21,23], 19) == 9

    def teste_4(self, pb):
        assert pb.pesquisa_binaria([1,3,5,7,9,11,13,15,17,19,21,23], -1) == None    
    