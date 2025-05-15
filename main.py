from swahili_spam_detector import logger
from swahili_spam_detector.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from swahili_spam_detector.pipeline.stage_02_data_processing import DataProcessingTrainingPipeline
from swahili_spam_detector.pipeline.stage_03_model_training import ModelTrainingPipeline
from swahili_spam_detector.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Processing stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_processing = DataProcessingTrainingPipeline()
    data_processing.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e

STAGE_NAME = "Model Training stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")   
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
