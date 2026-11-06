import pandas as pd

def pregunta_09():
    """
    Retorne la tabla `data/tbl0.tsv` completa con una columna adicional
    llamada `year`, al final, que contenga el año de la fecha de la columna
    `c3` como un texto de cuatro caracteres.

    Ejemplo del formato de la respuesta:

            c0 c1  c2          c3  year
        0    0  E   1  1999-02-28  1999
        1    1  A   2  1999-10-28  1999
        2    2  B   5  1998-05-02  1998
        ...
    """
    df_columna_año = pd.read_csv("data/tbl0.tsv", sep="\t") #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'df_columna_año'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    df_columna_año["year"] = df_columna_año["c3"].str.slice(0,4)        #? Crear una nueva columna llamada 'year' que extrae los primeros 4 caracteres de la columna 'c3' (que contiene fechas en formato 'YYYY-MM-DD'). Esto extrae el año de cada fecha.
        
    return df_columna_año
    

