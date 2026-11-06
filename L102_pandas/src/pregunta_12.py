import pandas as pd

def pregunta_12():
    """
    En `data/tbl2.tsv`, cada valor de la columna `c0` aparece en varias
    filas. Construya un DataFrame con una fila por cada valor de `c0`, en
    orden ascendente, y las columnas `c0` y `c5`. En `c5`, forme un texto
    `c5a:c5b` para cada fila de ese `c0`, ordene esos textos alfabéticamente y
    únalos separados por comas.

    Ejemplo del formato de la respuesta:

            c0                             c5
        0    0  bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
        1    1        aaa:3,ccc:2,ddd:0,hhh:9
        2    2        ccc:6,ddd:2,ggg:5,jjj:1
        ...
    """

    df_c0_listc5a_c5b_tbl2 = pd.read_csv("data/tbl2.tsv", sep="\t")      #? Leer el archivo `tbl2.tsv` y cargarlo en un DataFrame llamado 'df_c0_listc5a_c5b_tbl2'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
        #? Crear una nueva columna llamada 'c5' que concatene los valores de las columnas 'c5a' y 'c5b' separados por ':' usando el operador `+`. Convertir los valores de 'c5b' a cadenas con '.apply(str)' para asegurarse de que se puedan concatenar.
    df_c0_listc5a_c5b_tbl2["c5"] = df_c0_listc5a_c5b_tbl2["c5a"] + ":" + df_c0_listc5a_c5b_tbl2["c5b"].apply(str) 
        
    return df_c0_listc5a_c5b_tbl2.groupby("c0", as_index = False)[["c5"]].agg(lambda s: ",".join(sorted(s)))
        


    
