import pandas as pd

def pregunta_03():
    """
    Usando `data/tbl0.tsv`, cuente cuántos registros hay para cada categoría
    de la columna `c1`. Retorne una Serie de Pandas cuyo índice son las
    categorías, en orden alfabético, y cuyos valores son las cantidades.

    Ejemplo del formato de la respuesta:

        c1
        A     8
        B     7
        C     5
        ...
    """

    # Leer el archivo TSV
    df = pd.read_csv("data/tbl0.tsv", sep="\t")

    # Contar los registros por categoría en la columna 'c1'
    conteo = df['c1'].value_counts().sort_index()

    return conteo
