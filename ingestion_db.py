import pandas as pd
import os
import logging
import time
from sqlalchemy import create_engine

# Configure Logging
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Database Engine
engine = create_engine("sqlite:///inventory.db")


def ingest_db(df, table_name, engine=engine):
    """
    Ingest a DataFrame into a database table.
    """

    try:
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        logging.info(
            f"Successfully ingested data into '{table_name}' table."
        )

    except Exception as e:
        logging.error(
            f"Error ingesting data into '{table_name}': {e}"
        )
        raise


def load_raw_data():
    """
    Load all CSV files from the data folder
    and ingest them into SQLite tables.
    """

    start_time = time.time()

    try:

        for file in os.listdir("data"):

            if file.endswith(".csv"):

                file_path = os.path.join("data", file)

                logging.info(
                    f"Reading file: {file}"
                )

                df = pd.read_csv(file_path)

                table_name = file[:-4]

                ingest_db(
                    df=df,
                    table_name=table_name,
                    engine=engine
                )

        end_time = time.time()

        total_time = (end_time - start_time) / 60

        logging.info(
            "------------- Ingestion Complete -------------"
        )

        logging.info(
            f"Total Time Taken: {total_time:.2f} minutes"
        )

    except Exception as e:

        logging.error(
            f"Error during ingestion process: {e}"
        )

        raise


if __name__ == "__main__":
    load_raw_data()