import os
import glob
import pandas as pd


def pregunta_01():
    """
    Las frases de este laboratorio no están en una tabla, sino en miles de
    archivos de texto organizados en carpetas. Dentro de `data/` hay dos
    carpetas, `train/` y `test/`, y cada una contiene las carpetas
    `negative/`, `neutral/` y `positive/`. Cada archivo `.txt` contiene una
    frase, y la carpeta donde se encuentra indica su sentimiento.

    Su tarea es construir un dataset para cada división y guardarlo en:

    - `submission/train_dataset.csv`
    - `submission/test_dataset.csv`

    Cada archivo debe tener dos columnas: `phrase`, con el texto de la frase,
    y `target`, con el nombre de la carpeta de sentimiento (`negative`,
    `neutral` o `positive`). Recorra las carpetas y los archivos en orden
    alfabético, de modo que el resultado sea siempre el mismo. No guarde el
    índice de Pandas en el CSV.
    """
    # 1. Crear el directorio de salida si no existe
    os.makedirs("submission", exist_ok=True)

    # 2. Definir los splits a procesar (train y test)
    splits = ["train", "test"]

    for split in splits:
        records = []
        
        # 'negative', 'neutral', 'positive' en orden alfabético estricto
        sentiments = sorted(["negative", "neutral", "positive"])

        for sentiment in sentiments:
            # Construir la ruta de la carpeta
            folder_path = os.path.join("data", split, sentiment)
            
            # Obtener todos los archivos .txt y ordenarlos alfabéticamente
            txt_files = sorted(glob.glob(os.path.join(folder_path, "*.txt")))

            for file_path in txt_files:
                # Leer el contenido del archivo con codificación UTF-8
                with open(file_path, "r", encoding="utf-8") as file:
                    phrase = file.read().strip()
                    records.append({"phrase": phrase, "target": sentiment})

        # Crear el DataFrame de pandas
        df = pd.DataFrame(records)

        # Guardar en CSV omitiendo el índice y asegurando UTF-8
        output_path = os.path.join("submission", f"{split}_dataset.csv")
        df.to_csv(output_path, index=False, encoding="utf-8")

   