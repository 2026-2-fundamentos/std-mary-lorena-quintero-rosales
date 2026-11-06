import pandas as pd

def pregunta_10():
    """
    Usando `data/tbl0.tsv`, construya para cada categoría de la columna `c1`
    un texto con todos sus valores de la columna `c2`, ordenados de menor a
    mayor y separados por `:`. Retorne un DataFrame cuyo índice son las
    categorías, en orden alfabético, con una única columna llamada `c2`.

    Ejemplo del formato de la respuesta:

                           c2
        c1
        A     1:1:2:3:6:7:8:9
        B       1:3:4:5:6:8:9
        C           0:5:6:7:9
        ...
    """

    df_tablaC1_listaC2 = pd.read_csv("data/tbl0.tsv", sep="\t")     #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'df_count_c2'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    return df_tablaC1_listaC2.groupby("c1")[["c2"]].agg(func = lambda s: ":".join(sorted(s.map(str))))  #? Agrupar los datos por la columna 'c1' y para cada grupo de 'c1', aplicar una función que:
        

    
