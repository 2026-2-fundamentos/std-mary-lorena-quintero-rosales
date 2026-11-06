import pandas as pd

def pregunta_01():
    """
    ¿Cuántos registros tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
    como un número entero.

    Ejemplo del formato de la respuesta:

        40
    """

    # Leer el archivo `data/tbl0.tsv` y cargarlo en un DataFrame llamado 'cantidad'.
    cantidad = pd.read_csv("data/tbl0.tsv", sep="\t")  
    
    
    return cantidad.shape[0]

    
