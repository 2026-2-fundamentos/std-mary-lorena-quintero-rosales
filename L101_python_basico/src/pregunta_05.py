import gzip


def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.
    """
    Valores = {}

    with gzip.open("data/data.csv.gz", "rt") as file:
        lineas = file.readlines()

    for linea in lineas:
        partes = linea.strip().split()
        if not partes:
            continue

        letra = partes[0]
        valor = int(partes[1])

        if letra in Valores:
            Valores[letra].append(valor)
        else:
            Valores[letra] = [valor]

    resultado = []
    for letra in sorted(Valores.keys()):
        maximo_valor = max(Valores[letra])
        minimo_valor = min(Valores[letra])
        resultado.append((letra, maximo_valor, minimo_valor))

    return resultado