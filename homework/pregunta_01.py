import zipfile
import os
import csv

def pregunta_01():
    """
    La información requerida para este laboratorio está almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creará la carpeta "input" en la raíz del
    repositorio, la cual contiene la siguiente estructura de archivos:

    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            ...
        positive/
            0000.txt
            ...
        neutral/
            0000.txt
            ...

    A partir de esta información, escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "files/output" ubicada en la raíz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. Hay una frase por cada archivo de texto.
    * target: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.
    """

    # Ruta del archivo zip
    zip_file = "files/input.zip"
    # Ruta de destino donde se extraerán los archivos
    output_dir = "input"

    # Verificar si el archivo zip existe
    if not os.path.exists(zip_file):
        print(f"El archivo {zip_file} no existe.")
        return

    # Descomprimir el archivo
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
        print(f"El archivo {zip_file} ha sido descomprimido correctamente en {output_dir}")

    # Crear carpeta de salida si no existe
    output_dir_csv = "files/output"
    if not os.path.exists(output_dir_csv):
        os.makedirs(output_dir_csv)

    def generar_csv(input_dir, output_file):
        # Inicializar listas para frases y sentimientos
        phrases = []
        targets = []

        # Definir los subdirectorios que contienen los archivos de texto
        sentiment_dirs = ['positive', 'negative', 'neutral']

        # Recorrer las carpetas y agregar los datos
        for sentiment in sentiment_dirs:
            sentiment_path = os.path.join(input_dir, sentiment)
            
            if not os.path.exists(sentiment_path):
                print(f"El directorio {sentiment_path} no existe.")
                continue

            # Leer los archivos dentro de cada directorio
            for filename in os.listdir(sentiment_path):
                file_path = os.path.join(sentiment_path, filename)
                
                if os.path.isfile(file_path):
                    # Leer el contenido del archivo de texto
                    with open(file_path, 'r', encoding='utf-8') as file:
                        phrase = file.read().strip()
                        
                    # Añadir la frase y su sentimiento a las listas
                    phrases.append(phrase)
                    targets.append(sentiment)

        # Escribir los datos en un archivo CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['phrase', 'target'])
            writer.writerows(zip(phrases, targets))

    # Generar archivos CSV para train y test
    generar_csv(os.path.join(output_dir, 'input', 'train'), os.path.join(output_dir_csv, "train_dataset.csv"))
    generar_csv(os.path.join(output_dir, 'input', 'test'), os.path.join(output_dir_csv, "test_dataset.csv"))

    print("Archivos 'train_dataset.csv' y 'test_dataset.csv' generados correctamente en la carpeta 'files/output'.")

# Llamar a la función para ejecutar la descompresión y generación de archivos CSV
pregunta_01()