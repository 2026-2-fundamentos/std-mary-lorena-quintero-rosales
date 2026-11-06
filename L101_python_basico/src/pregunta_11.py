import gzip


def pregunta_11():
    """
    La cuarta columna (`codes`) contiene letras minúsculas separadas por
    comas. Para cada una de esas letras, sume los valores de la segunda
    columna (`value`) de los registros en los que aparece. Retorne un
    diccionario `{letra: suma}` con las letras en orden alfabético.
    """
    with gzip.open("data/data.csv.gz", "rt") as file:
        lineas = file.readlines()

    suma_por_letra = {}

    for linea in lineas:
        partes = linea.strip().split()
        if not partes:
            continue

        columna_2 = int(partes[1])
        columna_4 = partes[3].split(",")

        for letra in columna_4:
            if letra not in suma_por_letra:
                suma_por_letra[letra] = 0
            suma_por_letra[letra] += columna_2

    return dict(sorted(suma_por_letra.items()))
