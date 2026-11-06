import gzip


def pregunta_03():
    """
    Sume los valores de la segunda columna (`value`) para cada letra de la
    primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
    ordenada alfabeticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 53), ("B", 36), ("C", 27), ...]
    """

    Suma_Por_Letra = {}

    with gzip.open("data/data.csv.gz", "rt") as file:
        for linea in file:
            partes = linea.strip().split()
            if not partes:
                continue

            letra = partes[0]
            valor = int(partes[1])

            if letra in Suma_Por_Letra:
                Suma_Por_Letra[letra] += valor
            else:
                Suma_Por_Letra[letra] = valor

    resultado = sorted(Suma_Por_Letra.items())
    return resultado

    
