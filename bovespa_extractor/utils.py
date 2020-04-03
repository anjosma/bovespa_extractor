import json

def load_file_json(file_name):
    with open(file_name, 'r') as json_file:
        return json.load(json_file)

def load_file_url(file_name):
    with open(file_name, 'r') as f:
        return f.read()