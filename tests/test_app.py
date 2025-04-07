from src.app import add, sub
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_sub():
    assert sub(5 , 3) == 2
    assert sub(100 , 1) == 99

