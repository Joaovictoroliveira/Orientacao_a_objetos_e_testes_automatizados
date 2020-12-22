import pytest

def media(A, B):
    media = ((A * 4) + (B * 6)) // 10
    return media

def test_answer():
    assert(media(5,0)) == 2
