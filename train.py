import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'DATA', 'input.txt')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Loaded {len(text)} characters from {DATA_PATH}")
