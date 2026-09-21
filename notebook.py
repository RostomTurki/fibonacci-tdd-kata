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


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    def fibonacci(n: int) -> int:
        mo.md(r"""this function represents the logi of fibonacci""")
        #returns 0 if n==0 and 1 if n==1
        if n <= 1:
            return n
        #recursive method to compute a fibonacci number
        return fibonacci(n-1) + fibonacci(n-2)

    return (fibonacci,)


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

    return


@app.cell
def _():
    n = int(input())
    return (n,)


@app.cell
def _(fibonacci, mo, n):
    mo.md(f"""
    ### Fibonacci({n}) = {fibonacci(n)}
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
