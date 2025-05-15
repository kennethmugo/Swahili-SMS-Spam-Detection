# Swahili SMS Spam Detection

A machine learning system for detecting spam in Swahili SMS messages using state-of-the-art language models and MLOps practices.

## Project Overview

This project implements an end-to-end machine learning pipeline for detecting spam in Swahili text messages. It uses the LaBSE (Language-agnostic BERT Sentence Embeddings) model for text embedding and a binary classifier for spam detection.

### Key Features

- Multilingual text processing using LaBSE
- FastAPI-based REST API for real-time predictions
- MLflow for experiment tracking and model versioning
- DVC for data and model versioning
- Docker support for containerized deployment
- Modular architecture following clean code principles

## Technical Architecture

### Components

1. **Data Processing Pipeline**
   - Handles data ingestion and preprocessing
   - Generates embeddings using LaBSE model
   - Manages train-test splitting

2. **Model Pipeline**
   - Trains binary classifier on embeddings
   - Performs model evaluation
   - Logs metrics and artifacts to MLflow

3. **API Service**
   - FastAPI-based REST endpoint
   - Real-time prediction serving
   - Model loading and management

### Directory Structure

```
├── artifacts/          # Generated artifacts (data, models)
├── config/            # Configuration files
├── model/            # Saved models
├── research/         # Jupyter notebooks for experimentation
├── src/              # Main source code
│   └── swahili_spam_detector/
│       ├── components/    # Core ML components
│       ├── config/       # Configuration management
│       ├── constants/    # Project constants
│       ├── entity/      # Data classes and types
│       ├── pipeline/    # Training and prediction pipelines
│       └── utils/       # Utility functions
└── tests/           # Unit and integration tests
```

## Getting Started

### Prerequisites

- Python 3.10
- Conda (recommended for environment management)
- Git LFS (for model files)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kennethmugo/Swahili-SMS-Spam-Detection.git
cd Swahili-SMS-Spam-Detection
```

2. Create and activate conda environment:
```bash
conda create -n swahili_spam python=3.10
conda activate swahili_spam
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. **Local Development**:
```bash
uvicorn app:app --reload
```

2. **Docker Deployment**:
```bash
docker build -t swahili-spam-detector .
docker run -p 8000:8000 swahili-spam-detector
```

3. **View MLFlow Experiments**
```bash
mlflow server --host 127.0.0.1 --port 8080
```

## API Usage

### Endpoint: POST /predict

Predicts whether a given SMS is spam or not.

**Request**:
```json
{
    "text": "Your SMS message here"
}
```

**Response**:
```json
{
    "prediction": "spam",
    "score": 0.95
}
```

## Development Workflow

1. **Data Pipeline**:
   - Update data in `artifacts/data_ingestion/`
   - Run data processing pipeline: `python main.py`
   - DVC will track changes: `dvc add artifacts/data_ingestion`

2. **Model Training**:
   - Configure parameters in `params.yaml`
   - Run training pipeline: `python main.py` or `dvc repro`. If you are using the latter, run `dvc init` command first
   - MLflow will track experiments automatically

3. **Model Deployment**:
   - Best model is automatically saved to `model/`
   - Update API if needed in `app.py`
   - Build and deploy Docker container

## MLOps Features

### DVC Integration

- Data and model versioning
- Pipeline automation
- Experiment tracking

### MLflow Integration

- Experiment tracking
- Model registry
- Metric logging
- Artifact management

## Configuration

### params.yaml
Contains model hyperparameters and training configuration:
```yaml
EMBEDDING_MODEL: "sentence-transformers/LaBSE"
CLASSIFICATION_MODEL: "LogisticRegression"
  ...
```

### config/
Contains environment-specific configurations and paths.

## Acknowledgments

- LaBSE model from Google Research
- FastAPI framework
- MLflow and DVC communities
