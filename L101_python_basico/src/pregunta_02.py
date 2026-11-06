import gzip

def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
    alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 8), ("B", 7), ("C", 5), ...]
    """

    traductor = {}
    with gzip.open('data/data.csv.gz', 'rt') as file:
        for linea in file:
            datos = linea.split()
            letra = datos[0].strip()
            traductor[letra] = traductor.get(letra, 0) + 1

    res = sorted([(letra, cantidad) for letra, cantidad in traductor.items()])

    return res
