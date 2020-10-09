import fatorial_recursivo
import pytest

@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])

def testa_fatorial(entrada, esperado):
    assert(fatorial_recursivo.fatorial(entrada) == esperado)
