import sys
from pathlib import Path

from utils.file_reader.file_reader import read_file

if __name__ ==  '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py instance_name.txt")
        sys.exit(1)
    file_name = sys.argv[1]
    file_path = Path('../data/input/')/ file_name
    content = read_file(file_path)
    print(content)

