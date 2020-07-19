from bovespa_extractor.common.utils import create_dir, load_file_json
import requests
import zipfile
import io
import csv
import os

def get_company_data(url: str) -> requests.models.Response:
    return requests.get(url)

ENCODING = "ISO-8859-1"
CONFIG_CVM_PATH = "./configuration/extraction_cvm.json"

configs_cvm = load_file_json(CONFIG_CVM_PATH)

def download_txt_file():
    pass
def download_from_zip():
    for year in range(2010, 2021):

        file_z = get_company_data(url.format(year=year))
        
        zf = zipfile.ZipFile(io.BytesIO(file_z.content))
        files = [s for s in zf.namelist()]

        for data in files:
            file_path = os.path.join("data", "cvm", sortof.lower(), data)
            create_dir(file_path)
            with zf.open(data) as f1:
                with open(file_path, "w") as f:
                    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
                    writer.writerows(csv.reader(f1.read().decode(ENCODING).lower().splitlines(), delimiter=';'))

if __name__ == "__main__":

    for sortof in configs_cvm.keys():
        url = configs_cvm[sortof].get("URL")

        if ".txt" in url:
            download_txt()
        #elif ".zip" in url:
            #download_from_zip()

        
            