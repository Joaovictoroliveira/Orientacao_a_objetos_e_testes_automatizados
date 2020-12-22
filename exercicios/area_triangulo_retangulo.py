import pytest

def area_tr(A, B):
    area = (A * B) // 2
    return area

def test_answer():
    assert(area_tr(4,2)) == 4
