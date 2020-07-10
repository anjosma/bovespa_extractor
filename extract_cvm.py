import requests
import zipfile
import io
import csv

def get_company_data(url: str) -> requests.models.Response:
    return requests.get(url)

if __name__ == "__main__":

    file_z = get_company_data("http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DRE/DADOS/dre_cia_aberta_2019.zip")
    
    zf = zipfile.ZipFile(io.BytesIO(file_z.content))
    files = [s for s in zf.namelist()]

    for data in files:
        with zf.open(data) as f:
            with open("notebook/{}".format(data), "w") as f1:
                writer = csv.writer(f1, quoting=csv.QUOTE_MINIMAL)
                writer.writerows(csv.reader(f.read().decode("ISO-8859-1").lower().splitlines(), delimiter=';'))
        