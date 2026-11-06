import gzip


def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.
    """
    valores = {}

    with gzip.open("data/data.csv.gz", "rt") as file:
        lineas = file.readlines()

    for linea in lineas:
        partes = linea.strip().split()
        if not partes:
            continue

        columna5 = partes[4].split(",")

        for item in columna5:
            clave, valor = item.split(":")
            valor = int(valor)

            if clave in valores:
                valores[clave].append(valor)
            else:
                valores[clave] = [valor]

    resultado = []
    for clave in sorted(valores.keys()):
        valor_maximo = max(valores[clave])
        valor_minimo = min(valores[clave])
        resultado.append((clave, valor_minimo, valor_maximo))

    return resultado