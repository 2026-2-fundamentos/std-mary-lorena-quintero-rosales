import gzip


def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
    columna (`date`). Represente el mes como un texto de dos dígitos y retorne
    una lista de tuplas `(mes, cantidad)` ordenada por el mes.
    """
    Contar_Meses = {}

    with gzip.open("data/data.csv.gz", "rt") as file:
        lineas = file.readlines()

    for linea in lineas:
        partes = linea.strip().split()
        if not partes:
            continue

        fecha = partes[2]
        mes = fecha.split("-")[1]

        if mes in Contar_Meses:
            Contar_Meses[mes] += 1
        else:
            Contar_Meses[mes] = 1

    Resultado = sorted(Contar_Meses.items())
    return Resultado 
