from bovespa_extractor.common.utils import load_file_json, load_file_url, str_date_to_timestamp

CONFIG_MAIN_FILE = "./configuration/extraction_main.json"
CONFIG_STOCK_FILE = "./configuration/extraction_stocks.json"
URL_FILE = "url"

configs_main = load_file_json(CONFIG_MAIN_FILE)
configs_stock = load_file_json(CONFIG_STOCK_FILE)

date_start = configs_main.get("DATE_START")
date_end = configs_main.get("DATE_END")

def load_stocks_to_extract(file_name: str) -> list:
    return configs_main.get("EXTRACT_STOCKS")



if __name__ == "__main__":
    stocks = load_stocks_to_extract(CONFIG_MAIN_FILE)
    url = load_file_url(URL_FILE)
