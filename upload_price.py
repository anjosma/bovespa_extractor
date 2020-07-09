from bovespa_extractor.connection.database import Postgres
from bovespa_extractor.common.utils import load_file_json

import glob
import csv

configs_db = load_file_json("./configuration/database.json")
configs_main = load_file_json("./configuration/extraction_main.json")

data_stock_dir = configs_main.get("DATA_STOCK_DIR")
data_index_dir = configs_main.get("DATA_INDEX_DIR")

def upload_files_data_to_db(data_dir, schema):
    cursor = psql.get_cursor

    files_to_upload = [file for file in glob.glob("{dir}*.csv".format(dir=data_dir))]
    
    for file in files_to_upload:
        table_name = file.split("/")[-1].split(".")[0]
        
        cursor.execute(
            """
                CREATE TABLE {schema}.{table_name} (
                    date date PRIMARY KEY,
                    open float,
                    high float,
                    low float,
                    close float,
                    adj_close float,
                    volume float
                )
            """.format(schema=schema, table_name=table_name)
        )
        
        with open(file, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                row = [None if value == "" else value for value in row]
                cursor.execute(
                """
                INSERT INTO {schema}.{table_name} (date, open, high, low, close, adj_close, volume) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """.format(schema=schema, table_name=table_name),
                row
                )
        psql.commit()

if __name__ == "__main__":

    psql = Postgres(
        host=configs_db.get("HOST"),
        user=configs_db.get("USER"),
        password=configs_db.get("PASSWORD"),
        port=configs_db.get("PORT"),
        database=configs_db.get("DATABASE")
    )

    upload_files_data_to_db(data_stock_dir, "stocks")
    upload_files_data_to_db(data_index_dir, "indexes")

    psql.close()