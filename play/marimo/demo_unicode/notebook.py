import marimo

__generated_with = "0.23.2"
app = marimo.App(width="medium")


@app.cell
def _(DataFrame, generator):

    DataFrame(generator(as_dict=True))
    return


@app.cell
def _():
    from unicodedata import name, category
    from polars import DataFrame
    import marimo as mo

    def uname(c: str) -> str:
        "Input single character, get unicode name of character"
        try:
            return name(c)
        except ValueError:
            return ""

    def generator(as_dict=False):
        "Return unicode codepoint, character, name and category"
        cols = ("i", "chr", "name","category")
        it = range(100)
        for i in it:
            c = chr(i)
            if not c.isprintable():
                continue
            n = uname(c)
            if not n:
                continue
            row = (i,c,n,category(c))
            if as_dict:
                yield dict(zip(cols, row))
            else:
                yield row

    #uname("a")
    return DataFrame, generator


if __name__ == "__main__":
    app.run()
