from bovespa_extractor.common.utils import load_file_json, load_file_url, str_date_to_timestamp, create_dir

import requests
import csv

CONFIG_MAIN_FILE = "./configuration/extraction_main.json"
CONFIG_STOCK_FILE = "./configuration/extraction_stocks.json"
URL_FILE = "./configuration/url"
ENCODING = "UTF-8"
DATA_DIR = "./data/"

create_dir(DATA_DIR)

configs_main = load_file_json(CONFIG_MAIN_FILE)
configs_stock = load_file_json(CONFIG_STOCK_FILE)

date_start = configs_main.get("DATE_START")
date_end = configs_main.get("DATE_END")

def load_stocks_to_extract(file_name: str) -> list:
    return configs_main.get("EXTRACT_STOCKS")

def get_stock_data(stock: str) -> requests.models.Response:
    return requests.get(url.format(stock=stock, date_start=date_start_ts, date_end=date_end_ts))

def write_into_csv(data: requests.models.Response, file_name: str) -> None:
    with open(DATA_DIR+"{name}.csv".format(name=file_name), "w") as f:
        writer = csv.writer(f)
        writer.writerows(csv.reader(data.content.decode(ENCODING).splitlines(), delimiter=','))

def run_extraction_stock(stocks):
    for stock in stocks:
        data = get_stock_data(stock)
        write_into_csv(data, stock)

if __name__ == "__main__":
    stocks = load_stocks_to_extract(CONFIG_MAIN_FILE)
    url = load_file_url(URL_FILE)

    date_start_ts = str_date_to_timestamp(date_start)
    date_end_ts = str_date_to_timestamp(date_end)

    run_extraction_stock(stocks)
