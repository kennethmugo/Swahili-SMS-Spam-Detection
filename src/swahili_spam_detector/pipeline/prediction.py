import joblib
from sentence_transformers import SentenceTransformer
import torch

class PredictionPipeline:
    def __init__(self, embedding_model: str, classifier_model_path: str):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        # Load models once during initialization
        self.embedder = SentenceTransformer(embedding_model, device=device)
        self.classifier = joblib.load(classifier_model_path)

    def predict(self, text: str) -> float:
        embedding = self.embedder.encode(text)
        prediction = self.classifier.predict_proba([embedding])[0][1]
        return prediction
