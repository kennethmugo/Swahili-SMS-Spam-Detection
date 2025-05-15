import os
import joblib
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from swahili_spam_detector.entity.config_entity import ModelTrainingConfig
from swahili_spam_detector.utils.common import save_json


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train_model(self):
        # Load saved embeddings
        train_data_path = os.path.join(self.config.train_data_path, self.config.sms_embeddings_filename)
        train_labels_path = os.path.join(self.config.train_data_path, self.config.labels_filename)

        X = np.load(train_data_path)
        y = np.load(train_labels_path)

        # Split the data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        # Initialize the model
        model = LogisticRegression(max_iter=100)

        # Train the model
        model.fit(X_train, y_train)

        ## Generate a classification report
        y_pred = model.predict(X_val)
        report = classification_report(y_val, y_pred, output_dict=True)

        # save the report
        save_json(Path(self.config.report_path), report)

        # save the model
        joblib.dump(model, self.config.trained_model_path)

