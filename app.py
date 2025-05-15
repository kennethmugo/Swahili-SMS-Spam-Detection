from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
from src.swahili_spam_detector.pipeline.prediction import PredictionPipeline

ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    predictor = PredictionPipeline(
        embedding_model="sentence-transformers/LaBSE",
        classifier_model_path="model/model.joblib"
    )
    ml_models["predictor"] = predictor
    yield

    # Shutdown
    ml_models.clear()

app = FastAPI(title="Swahili Spam Detector API", lifespan=lifespan)

class Text(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str
    score: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(text: Text):
    predictor = ml_models["predictor"]
    prediction = predictor.predict(text.text)
    result = "spam" if prediction >= 0.5 else "ham"

    return PredictionResponse(prediction=result, score=prediction)