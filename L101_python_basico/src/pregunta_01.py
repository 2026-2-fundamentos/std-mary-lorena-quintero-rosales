
import gzip

def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.
    """
    with gzip.open('data/data.csv.gz', 'rt') as file:
        suma = 0
        for linea in file:
            datos = linea.split()
            suma += int(datos[1])

        return suma