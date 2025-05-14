import pandas as pd
import os
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split
from swahili_spam_detector import logger
from swahili_spam_detector.entity.config_entity import DataProcessingConfig

class DataProcessing:
    def __init__(self, config: DataProcessingConfig):
        self.config = config
        self.model = SentenceTransformer(self.config.embedding_model)
    
    def process_data(self):
        """
        Process the data by generating embeddings and saving the processed data to npy files.
        """
        df = pd.read_csv(self.config.raw_data_path)

        logger.info("Embeddings being generated...")

        X = self.generate_embeddings_batch(df['Sms'].tolist())
        logger.info("Embeddings generated")

        y = (df['Category'] == 'scam').astype(int)  # Convert labels to binary
        logger.info("Labels generated")

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        self.save_data(X_train, y_train, is_train=True)
        self.save_data(X_test, y_test, is_train=False)

    def generate_embeddings_batch(self, texts, batch_size=32) -> np.ndarray:
        """Generate embeddings in batches to manage memory"""
        all_embeddings = []
        
        for i in tqdm(range(0, len(texts), batch_size)):
            batch = texts[i:i + batch_size]
            embeddings = self.model.encode(batch)
            all_embeddings.append(embeddings)
            
        return np.vstack(all_embeddings)
    
    def save_data(self, X, y, is_train: bool):
        """Save the data to a npy files"""
        if is_train:
            train_data_path = os.path.join(self.config.train_data_path, self.config.sms_embeddings_filename)
            np.save(train_data_path, X)
            train_labels_path = os.path.join(self.config.train_data_path, self.config.labels_filename)
            np.save(train_labels_path, y)
        else:
            test_data_path = os.path.join(self.config.test_data_path, self.config.sms_embeddings_filename)
            np.save(test_data_path, X)
            test_labels_path = os.path.join(self.config.test_data_path, self.config.labels_filename)
            np.save(test_labels_path, y)

