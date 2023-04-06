import sys


def txt_importer(path_file: str):
    file_extension = str(path_file).split(".")[-1]
    if file_extension != 'txt':
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, encoding="utf-8") as txt_file:
            text = [
                text.strip() for text in txt_file
            ]
            return text
    except (IsADirectoryError, FileNotFoundError):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
