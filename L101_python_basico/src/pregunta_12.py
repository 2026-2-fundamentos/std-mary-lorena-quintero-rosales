import gzip


def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.
    """
    with gzip.open("data/data.csv.gz", "rt") as file:
        lineas = file.readlines()

    suma_por_letra = {}

    for linea in lineas:
        partes = linea.strip().split()
        if not partes:
            continue

        letra = partes[0]
        columna_5 = partes[4].split(",")

        suma_columna_5 = sum(int(valor.split(":")[1]) for valor in columna_5)

        if letra not in suma_por_letra:
            suma_por_letra[letra] = 0
        suma_por_letra[letra] += suma_columna_5

    return dict(sorted(suma_por_letra.items()))