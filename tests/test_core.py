# tests/test_core.py
import pytest

from fibonacci_kata.core import fibonacci


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55),
        (50, 12586269025),
        (100, 354224848179261915075),
        (200, 280571172992510140037611932413038677189525),
    ],
)
def test_cases(n, expected):
    assert fibonacci(n) == expected
