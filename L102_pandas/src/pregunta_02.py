import pandas as pd

def pregunta_02():
    """
    ¿Cuántas columnas tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        4
    """

    # Leer el archivo TSV
    df = pd.read_csv('data/tbl0.tsv', sep='\t')

    # Contar el número de columnas
    num_columnas = df.shape[1]

    return num_columnas
