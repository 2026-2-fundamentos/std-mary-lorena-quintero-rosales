import pandas as pd

def pregunta_08():
    """
    Retorne la tabla `data/tbl0.tsv` completa con una columna adicional
    llamada `suma`, al final, cuyo valor en cada fila es `c0 + c2`.

    Ejemplo del formato de la respuesta:

            c0 c1  c2          c3  suma
        0    0  E   1  1999-02-28     1
        1    1  A   2  1999-10-28     3
        2    2  B   5  1998-05-02     7
        ...
    """

    df_suma_C0_C2 = pd.read_csv("data/tbl0.tsv", sep="\t")  #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'df_suma_C0_C2'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    df_suma_C0_C2["suma"] = df_suma_C0_C2["c0"] + df_suma_C0_C2["c2"]    #? Crear una nueva columna llamada 'suma' que contenga la suma de los valores de las columnas 'c0' y 'c2' en cada fila
    return df_suma_C0_C2

    
