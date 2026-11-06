import gzip


def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.
    """
    with gzip.open("data/data.csv.gz", "rt") as file:
        lineas = file.readlines()

    resultado = {}

    for linea in lineas:
        partes = linea.strip().split()
        if not partes:
            continue

        letra = partes[0]
        numero = int(partes[1])

        if numero not in resultado:
            resultado[numero] = set()
        resultado[numero].add(letra)

    rta = [(num, sorted(letras)) for num, letras in sorted(resultado.items())]
    return rta