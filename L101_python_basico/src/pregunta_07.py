import gzip
from collections import defaultdict


def pregunta_07():
    """
    Para cada valor distinto de la segunda columna (`value`), construya la
    lista de letras de la primera columna (`letter`) que aparecen con ese
    valor. Conserve las letras repetidas y el orden en que aparecen en el
    archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
    valor.
    """
    diccionario = defaultdict(list)

    with gzip.open("data/data.csv.gz", "rt") as file:
        for linea in file:
            datos = linea.split()
            if not datos:
                continue

            letra = datos[0]
            valor = int(datos[1])

            diccionario[valor].append(letra)

    return sorted(diccionario.items())