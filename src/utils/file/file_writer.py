from pathlib import Path

def write_file(file_path: Path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")

