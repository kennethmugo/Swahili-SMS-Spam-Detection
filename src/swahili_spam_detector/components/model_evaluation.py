import os
import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from swahili_spam_detector.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self):
        self.model = joblib.load(self.config.trained_model_path)

        # Load the test data
        test_data_path = os.path.join(self.config.test_data_path, self.config.sms_embeddings_filename)
        test_labels_path = os.path.join(self.config.test_data_path, self.config.labels_filename)

        X_test = np.load(test_data_path)
        y_test = np.load(test_labels_path)

        # Evaluate the model
        y_pred = self.model.predict(X_test)

        # calculate the metrics
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        accuracy = accuracy_score(y_test, y_pred)

        report = {
            "recall": recall,
            "precision": precision,
            "f1": f1,
            "accuracy": accuracy
        }

        self.report = report
    
    def log_into_mlflow(self):
        with mlflow.start_run(run_name=self.config.mlflow_experiment_name):
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(self.report)
            
            # Create model directory if it doesn't exist
            model_dir = "model"
            if not os.path.exists(model_dir):
                os.makedirs(model_dir)
            
            # Save and log the model
            model_path = os.path.join(model_dir, "model.joblib")
            joblib.dump(self.model, model_path)
            mlflow.log_artifact(model_path)
        
        
