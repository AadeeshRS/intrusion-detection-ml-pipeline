from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_validation import DataValidationConfig
from src.exception.exception import NetworkSecurityException
from src.logging.logger import logging
from src.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataTransformationConfig
import sys
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(
            training_pipeline_config=trainingpipelineconfig
        )
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data Ingestion")
        dataingstionartifact = data_ingestion.initate_data_ingestion()
        logging.info("Data Initiation completed")
        print(dataingstionartifact)
        datavalidationconfig = DataValidationConfig(
            training_pipeline_config=trainingpipelineconfig
        )
        data_validation = DataValidation(dataingstionartifact, datavalidationconfig)
        logging.info("Initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)
        logging.info("Initiate the data Transformation")
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("Data Transformation completed")
        print(data_transformation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
