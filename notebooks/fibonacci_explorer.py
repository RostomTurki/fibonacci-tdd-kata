import sys

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:
    from collections import Counter

    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_kata import fibonacci


@app.cell
def _():
    mo.md("""
    # Fibonacci Explorer

    Pick a range below and explore the Fibonacci numbers returned
    by your installed `fibonacci_kata` package.

    This notebook imports the function rather than reimplementing it.
    """)
    return


@app.cell
def _():
    start = mo.ui.slider(1, 200, value=1, label="Range start")
    end = mo.ui.slider(1, 200, value=100, label="Range end")
    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, start):
    lo, hi = sorted((start.value, end.value))
    results = [fibonacci(n) for n in range(lo, hi + 1)]
    results
    return (results,)


@app.cell
def _(results):
    counts = Counter(str(r) for r in results)

    fig, ax = plt.subplots()
    ax.bar(
        counts.keys(),
        counts.values(),
        color=["#4c72b0", "#dd8452", "#55a868", "#c44e52"],
    )
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Fibonacci outputs")
    fig
    return


@app.cell
async def _():

    if sys.platform == "emscripten":
        import micropip
        from js import location

        base = location.href.split("?")[0].split("#")[0].rsplit("/", 1)[0]
        await micropip.install(f"{base}/public/fibonacci_kata-0.1.0-py3-none-any.whl")
    from fibonacci_kata import fibonacci

    return (fibonacci,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
