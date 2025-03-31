from pathlib import Path

def read_file(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied for file '{file_path}'.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while reading the file '{file_path}': {e}")
