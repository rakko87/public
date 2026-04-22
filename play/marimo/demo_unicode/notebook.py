import marimo

__generated_with = "0.23.2"
app = marimo.App(width="medium")


@app.cell
def _(codepoints, df, is_python_id, mo):
    stack = mo.vstack(
        [
    codepoints, mo.ui.dataframe(df),is_python_id
        ],
    )

    stack
    return


@app.cell
def _():
    import marimo as mo

    from unicodedata import name, category
    from polars import DataFrame

    UNICODE_MAX = 0x110000



    def uname(c: str) -> str:
        "Input single character, get unicode name of character"
        try:
            return name(c)
        except ValueError:
            return ""



    def filter(it):
        for i in it:
            c = chr(i)

            if not c.isprintable():
                continue
            n = uname(c)
            if not n:
                continue
            yield (i,c,n,category(c))

    def demo():
        for r in filter(range(UNICODE_MAX)):
            pass
        print(r)



    demo()
    #uname("a")
    return DataFrame, filter, mo


@app.cell
def _(DataFrame, codepoints, filter, is_python_id):
    def generator(as_dict=False):
        "Return unicode codepoint, character, name and category"
        cols = ("i", "chr", "name","category")
        it = range(*codepoints.value)
        if is_python_id.value:
            it = (i for i in it if chr(i).isidentifier())
            
        for row in filter(it):
            if as_dict:
                yield dict(zip(cols, row))
            else:
                yield row

    df = DataFrame(generator(as_dict=True))

    return (df,)


@app.cell
def _(mo):
    codepoints = mo.ui.range_slider(
        label="Unicode points",
        start=0, 
        stop=1_000, 
        step=50, 
        value=[0, 200], 
        full_width=True,
    )

    is_python_id = mo.ui.checkbox(label="Is Python variable",value=True)
    return codepoints, is_python_id


if __name__ == "__main__":
    app.run()
