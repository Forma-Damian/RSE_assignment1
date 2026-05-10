import pytest
# Notice there is NO "src." in the import. It is just the package name!
from hello_numba.taylor_expansion import taylor_expansion_sin, math_func

def test_taylor_expansion():
    # Test the Taylor expansion of sin(x) around x=0
    x = 0.5
    n = 5
    expected = math_func(x)
    result = taylor_expansion_sin(x, n)
    assert abs(result - expected) < 1e-6, f"Expected {expected}, got {result}"

def test_math_func():
    # Test the math_func for a known value
    x = 0.5
    expected = 0.479425538604203
    result = math_func(x)
    assert abs(result - expected) < 1e-6, f"Expected {expected}, got {result}"