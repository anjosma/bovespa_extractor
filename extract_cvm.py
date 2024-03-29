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
    file_txt = get_company_data(url).content
    file_path = os.path.join("data", "cvm", sortof.lower(), url.split("/")[-1])
    create_dir(file_path)
    with open(file_path, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(csv.reader(file_txt.decode(ENCODING).splitlines(), delimiter=";"))

def download_from_zip():
    for year in range(2000, 2010):

        file_z = get_company_data(url.format(year=year))
        
        try:
            zf = zipfile.ZipFile(io.BytesIO(file_z.content))
            files = [s for s in zf.namelist()]

            for data in files:
                file_path = os.path.join("data", "cvm", sortof.lower(), data)
                create_dir(file_path)
                with zf.open(data) as f1:
                    with open(file_path, "w") as f:
                        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
                        writer.writerows(csv.reader(f1.read().decode(ENCODING).splitlines(), delimiter=';'))
        except:
            print("erro", url)    

if __name__ == "__main__":

    for sortof in configs_cvm.keys():
        url = configs_cvm[sortof].get("URL")

        if ".csv" in url:
            download_txt_file()
        elif ".zip" in url:
            download_from_zip()