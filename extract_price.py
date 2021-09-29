from bovespa_extractor.common.utils import load_file_json, load_file_url, str_date_to_timestamp, create_dir

import time
import requests
from datetime import datetime
import csv

CONFIG_MAIN_FILE = "./configuration/extraction_price.json"
URL_FILE = "./configuration/url"
ENCODING = "UTF-8"
STOCK_SUFFIX = ".SA"
INDEX_PREFIX = "%5E"
DATE_FORMAT = "%Y-%m-%d"

configs_main = load_file_json(CONFIG_MAIN_FILE)

data_stock_dir = configs_main.get("DATA_STOCK_DIR")
data_index_dir = configs_main.get("DATA_INDEX_DIR")
[create_dir(dirr) for dirr in [data_stock_dir, data_index_dir]]

date_start = configs_main.get("DATE_START")
date_end = configs_main.get("DATE_END")
if date_end == 'last': date_end = datetime.date(datetime.now()).strftime(DATE_FORMAT)

def load_stocks_to_extract(file_name: str) -> list:
    return [s + STOCK_SUFFIX for s in configs_main.get("EXTRACT_STOCKS")]

def load_index_to_extract(file_name: str) -> list:
    return [INDEX_PREFIX + i for i in  configs_main.get("EXTRACT_INDEX")]

def get_stock_data(stock: str) -> requests.models.Response:
    return requests.get(url.format(stock=stock, date_start=date_start_ts, date_end=date_end_ts))

def write_into_csv(response: requests.models.Response, file_name: str, storage_dir: str) -> None:
    with open(storage_dir+"{name}.csv".format(name=file_name), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        v = csv.reader(response.content.decode(ENCODING).replace(
            "null", "").replace(" ", "_").lower().splitlines(), delimiter=',')
        writer.writerows(v)

def run_extraction(names: list, storage_dir: str) -> None:
    for name in names:
        print(name)
        response = get_stock_data(name)
        write_into_csv(response, name.replace(STOCK_SUFFIX, "").replace(INDEX_PREFIX, ""), storage_dir)
        time.sleep(2.5)

if __name__ == "__main__":
    stocks = list(dict.fromkeys(load_stocks_to_extract(CONFIG_MAIN_FILE)))
    indexes = list(dict.fromkeys(load_index_to_extract(CONFIG_MAIN_FILE)))

    url = load_file_url(URL_FILE)

    date_start_ts = str_date_to_timestamp(date_start, DATE_FORMAT)
    date_end_ts = str_date_to_timestamp(date_end, DATE_FORMAT)

    run_extraction(stocks, data_stock_dir)
    run_extraction(indexes, data_index_dir)
