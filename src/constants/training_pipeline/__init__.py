import os,sys
import pandas as pd
import numpy as np

TARGET_COLUMNS="Result"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
FILE_NAME:str="phisingData.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

SCHEMA_FILE_PATH=os.path.join('data_schema',"schema.yaml")

DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="AADEESHAI"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2

DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_VALID_SIR:str="validated"
DATA_VALIDATION_INAVLID_DIR:str="invalid"
DATA_VALIDATION_DRFIT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRFIT_REPORT_FILE_NAME:str="report.yaml"