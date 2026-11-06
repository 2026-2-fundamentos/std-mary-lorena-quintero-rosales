import gzip


def pregunta_10():
    """
    Para cada registro del archivo, en el mismo orden en que aparecen,
    retorne una tupla con la letra de la primera columna (`letter`), la
    cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
    pares de la quinta columna (`metrics`). El resultado es una lista con una
    tupla por registro.
    """
    with gzip.open("data/data.csv.gz", "rt") as file:
        lineas = file.readlines()

    Rta = []

    for linea in lineas:
        partes = linea.strip().split()
        if not partes:
            continue

        letra = partes[0]
        columna_4 = partes[3].split(",")
        columna_5 = partes[4].split(",")

        Rta.append((letra, len(columna_4), len(columna_5)))

    return Rta