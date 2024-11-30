import os
import json
def save_data(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data(path, default_data):
    if not os.path.exists(path):
        save_data(path, default_data)
        return default_data
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
