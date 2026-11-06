import gzip


def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.
    """
    with gzip.open("data/data.csv.gz", "rt") as file:
        lineas = file.readlines()

    counter = {}

    for linea in lineas:
        partes = linea.strip().split()
        if not partes:
            continue

        columna_5 = partes[4]
        pares = columna_5.split(",")

        for par in pares:
            clave, _ = par.split(":")
            if clave not in counter:
                counter[clave] = 0
            counter[clave] += 1

    return dict(sorted(counter.items()))