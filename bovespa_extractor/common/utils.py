import json
import time
from datetime import datetime

def load_file_json(file_name: str) -> dict:
    with open(file_name, 'r') as json_file:
        return json.load(json_file)

def load_file_url(file_name: str) -> str:
    with open(file_name, 'r') as f:
        return f.read()

def str_date_to_timestamp(date: str, date_format: str = "%Y-%m-%d") -> int:
    return int(datetime.timestamp(datetime.strptime(date, date_format)))