import pandas as pd
import re 

def pregunta_01():
    """
    El archivo `data/clusters_report.txt` es un reporte de clústeres de
    palabras clave pensado para ser leído por una persona, no por un programa:
    los encabezados ocupan varias líneas, las columnas están alineadas con
    espacios y la lista de palabras clave de un clúster continúa en las líneas
    siguientes.

    Su tarea es convertir ese reporte en un DataFrame de Pandas con una fila
    por clúster y las columnas:

    - `cluster`: número del clúster, como entero.
    - `cantidad_de_palabras_clave`: como entero.
    - `porcentaje_de_palabras_clave`: como número decimal; por ejemplo, el
      texto `15,9 %` debe quedar como `15.9`.
    - `principales_palabras_clave`: todas las palabras clave del clúster en un
      solo texto, separadas por una coma y un único espacio.

    Retorne el DataFrame.

    Ejemplo del formato de la respuesta (se omite la última columna):

           cluster  cantidad_de_palabras_clave  porcentaje_de_palabras_clave
        0        1                         105                          15.9
        1        2                         102                          15.4
        ...
    """

    with open("data/clusters_report.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    data = []
    cluster = None
    cantidad_palabras = None
    porcentaje_palabras = None
    palabras_clave = []

    for linea in lineas[4:]:
        linea_str = linea.strip()

        # Si la línea está vacía y tenemos un clúster acumulado, guardamos
        if not linea_str:
            if cluster is not None:
                texto_palabras = " ".join(palabras_clave)
                # Reemplazar múltiples espacios por uno solo
                texto_palabras = re.sub(r"\s+", " ", texto_palabras)
                # Quitar el punto final si existe
                if texto_palabras.endswith("."):
                    texto_palabras = texto_palabras[:-1]

                data.append({
                    "cluster": cluster,
                    "cantidad_de_palabras_clave": cantidad_palabras,
                    "porcentaje_de_palabras_clave": porcentaje_palabras,
                    "principales_palabras_clave": texto_palabras.strip()
                })
                cluster = None
                palabras_clave = []
            continue

        partes = linea_str.split()

        # Inicio de un nuevo clúster
        if partes[0].isdigit():
            cluster = int(partes[0])
            cantidad_palabras = int(partes[1])
            porcentaje_palabras = float(partes[2].replace(",", "."))
            # Las palabras clave comienzan a partir de la 4ta o 5ta posición dependiendo si % está separado
            idx_palabras = 4 if partes[3] == "%" else 3
            palabras_clave.append(" ".join(partes[idx_palabras:]))
        else:
            # Línea de continuación de palabras clave
            palabras_clave.append(" ".join(partes))

    # Guardar el último clúster si no terminó en línea vacía
    if cluster is not None:
        texto_palabras = " ".join(palabras_clave)
        texto_palabras = re.sub(r"\s+", " ", texto_palabras)
        if texto_palabras.endswith("."):
            texto_palabras = texto_palabras[:-1]

        data.append({
            "cluster": cluster,
            "cantidad_de_palabras_clave": cantidad_palabras,
            "porcentaje_de_palabras_clave": porcentaje_palabras,
            "principales_palabras_clave": texto_palabras.strip()
        })

    df = pd.DataFrame(data)
    return df