# contents of text_sample.py
import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5


pytest.main(["-v", "--tb=line", "-rN", "test_sample.py"])