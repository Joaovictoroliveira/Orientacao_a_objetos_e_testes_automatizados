import pytest

def second_largest(lista):
    lista.remove(max(lista))
    return max(lista)

def test_answer():
    assert(second_largest([25, 143, 89, 13, 105])) == 105
