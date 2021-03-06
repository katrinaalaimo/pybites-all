from fibonacci import fib
import pytest


def test_fib(n):
    try:
        assert fib(0) == 0
        assert fib(1) == 1
        assert fib(6) == 8
    except ValueError:
        pytest.fail("Value Error")


