from bovespa_extractor.utils import load_file_json, load_file_url

CONFIG_FILE = "./configuration/extraction.json"
URL_FILE = "url"

configs = load_file_url(CONFIG_FILE)

def load_stocks(file_name):
    return [configs.get("STOCKS")]


if __name__ == "__main__":
    stocks = load_stocks(CONFIG_FILE)
    url = load_file_url(URL_FILE)
    
    