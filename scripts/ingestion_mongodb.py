import os
from dotenv import load_dotenv
import pandas as pd
from pymongo import MongoClient
from pathlib import Path


class MongoDatabase:
    def __init__(self, db_config):
        self.user = db_config["user"]
        self.password = db_config["password"]
        self.host = db_config["host"]
        self.port = db_config["port"]
        self.database = db_config["database"]
        self.client = None
        self.db = None

    def connect(self):
        uri = f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/?authSource=admin"
        self.client = MongoClient(uri)
        self.db = self.client[self.database]

    def is_connected(self):
        return self.client is not None

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close(self):
        self.client.close()
        self.client = None
        self.db = None


load_dotenv()
MONGO_CONFIG = {
    "user": os.getenv("MONGO_INITDB_ROOT_USERNAME"),
    "password": os.getenv("MONGO_INITDB_ROOT_PASSWORD"),
    "host": "localhost",
    "port": int(os.getenv("MONGO_PORT")),
    "database": "diabetes_db"
}


class MongoExecutor:
    def __init__(self, database, collection_name):
        self.db = database
        self.collection = database.get_collection(collection_name)

    def select(self, filter_query=None, projection=None, limit=10):
        return list(self.collection.find(filter_query or {}, projection).limit(limit))

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def update_one(self, filter_query, update_query):
        return self.collection.update_one(filter_query, update_query)

    def delete_one(self, filter_query):
        return self.collection.delete_one(filter_query)

    def count_documents(self, filter_query=None):
        return self.collection.count_documents(filter_query or {})


def map_external_record(record, dataset_name, row_number):
    document = {
        "external_id": f"{dataset_name}-{row_number:05d}",
        "source_file": record["source_file"],
        "pregnancies": int(record["pregnancies"]),
        "glucose": float(record["glucose"]),
        "blood_pressure": float(record["blood_pressure"]),
        "skin_thickness": float(record["skin_thickness"]),
        "insulin": float(record["insulin"]),
        "body_mass_index": float(record["body_mass_index"]),
        "diabetes_pedigree_function": float(record["diabetes_pedigree_function"]),
        "age": int(record["age"]),
        "outcome": int(record["outcome"]),
        "bmi_category": record["bmi_category"],
        "clinic_region": record["clinic_region"],
        "care_path": record["care_path"],
        "patient_segment": record["patient_segment"],
    }
    return document


def ingest_data(executor, csv_path, limit=None):
    df = pd.read_csv(csv_path)
    if limit:
        df = df.head(limit)
    documents = [map_external_record(row, "DIABETES", i) for i, row in enumerate(df.to_dict(orient="records"), start=1)]
    result = executor.insert_many(documents)
    return len(result.inserted_ids)


my_mongo = MongoDatabase(MONGO_CONFIG)
my_mongo.connect()
executor = MongoExecutor(my_mongo, "patients")
ingest_data(executor, "../raw/diabetes/diabetes-clean.csv")
my_mongo.close()
