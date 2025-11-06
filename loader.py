import json 

def muat_matakuliah(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def muat_aturan(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
