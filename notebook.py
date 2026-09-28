import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fibonacci Numbers

    The Fibonacci sequence is defined as:

    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    This notebook implements a function to compute the nth Fibonacci number and verifies its behavior with tests.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Imports
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pytest
    import sys
    sys.set_int_max_str_digits(10000000)
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fibonacci Fucntion
    """)
    return


@app.cell
def _():
    from functools import lru_cache
    #optimized version using cache
    @lru_cache(None)
    def fibonacci(n: int):
        a, b = 0, 1
        if n <= 1:
            return n
        for _ in range(n):
            a, b = b, a + b
        return a

    return (fibonacci,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tests
    """)
    return


@app.cell
def _():
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

    return (fibonacci,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Widget
    """)
    return


@app.cell
def _():
    n = int(input())
    return (n,)


@app.cell
def _(fibonacci, mo, n):
    mo.md(f"""
    #### Fibonacci({n}) = {fibonacci(n)}
    """)
    return


if __name__ == "__main__":
    app.run()
