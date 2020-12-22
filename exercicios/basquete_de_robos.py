import pytest

def pontuacao(D):
    if D > 1400:
        return 3
    elif D > 800:
        return 2
    return 1

def test_answer():
    assert(pontuacao(1720)) == 3
