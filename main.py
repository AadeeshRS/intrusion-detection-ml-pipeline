from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_validation import DataValidationConfig
from src.exception.exception import NetworkSecurityException
from src.logging.logger import logging
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        datavalidationconfig=DataValidationConfig(training_pipeline_config=trainingpipelineconfig)
        logging.info("Initiate the data Ingestion")
        dataingstionartifact=data_ingestion.initate_data_ingestion()
        logging.info("Data Initiation completed")
        print(dataingstionartifact)
        data_validation = DataValidation(dataingstionartifact, datavalidationconfig)
        logging.info("Initiate the data validation")
        data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(datavalidationconfig)

    except Exception as e:
        raise NetworkSecurityException(e,sys)