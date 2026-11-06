import pandas as pd

def pregunta_05():
    """
    Usando `data/tbl0.tsv`, encuentre el valor máximo de la columna `c2` para
    cada categoría de la columna `c1`. Retorne una Serie de Pandas cuyo índice
    son las categorías, en orden alfabético, y cuyos valores son los máximos.

    Ejemplo del formato de la respuesta:

        c1
        A    9
        B    9
        C    9
        ...
    """

    # Leer el archivo tbl0.tsv
    df = pd.read_csv("data/tbl0.tsv", sep="\t")

    # Agrupar por la columna 'c1' y obtener el valor máximo de 'c2'
    max_values = df.groupby('c1')['c2'].max()

    # Ordenar el índice alfabéticamente
    max_values = max_values.sort_index()

    return max_values
