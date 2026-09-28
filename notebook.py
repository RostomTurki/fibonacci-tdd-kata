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
def _(fibonacci):
    def test_fibonacci_0():
        assert fibonacci(0) == 0

    def test_fibonacci_1():
        assert fibonacci(1) == 1

    def test_fibonacci_5():
        assert fibonacci(5) == 5

    def test_fibonacci_10():
        assert fibonacci(10) == 55

    def test_fibonacci_20():
        assert fibonacci(20) == 6765


    def test_fibonacci_30():
        assert fibonacci(30) == 832040

    return


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
