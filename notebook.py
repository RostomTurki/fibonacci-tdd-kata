import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo


    return


@app.function
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@app.cell
def _():
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
    return


if __name__ == "__main__":
    app.run()
