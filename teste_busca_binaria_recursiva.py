import busca_binaria_recursiva
import pytest

lista = [10,20,30,40,50,60]

@pytest.mark.parametrize("lista, valor, esperado", [
    (lista, 10, 0),
    (lista, 20, 1),
    (lista, 30, 2),
    (lista, 40, 3),
    (lista, 50, 4),
    (lista, 60, 5),
    (lista, 70, False),
    (lista, 15, False),
    (lista, -10, False)
])

def testa_busca_binaria(lista, valor, esperado):
    assert(busca_binaria_recursiva.busca_binaria(lista, valor) == esperado)
