from main import fibonacci_1 as fibonacci
import pytest


def test_fibonacci_1_is_1():
    assert 1 == fibonacci(1)


def test_fibonacci_9_is_34():
    assert 34 == fibonacci(9)


def test_fibonacci_Negative():
    with pytest.raises(ValueError):
        fibonacci(-10)
