# Swahili SMS Spam Detection

## Project Overview

This project implements an end-to-end machine learning pipeline for detecting spam in Swahili text messages. It uses the LaBSE (Language-agnostic BERT Sentence Embeddings) model for text embedding and a binary classifier for spam detection.

### Key Features

- Multilingual text processing using LaBSE
- FastAPI-based REST API for real-time predictions
- MLflow for experiment tracking and model versioning
- DVC for data and model versioning
- Docker support for containerized deployment
- Modular architecture following clean code principles

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

3. **View MLFlow Experiments**:
```bash
mlflow server --host 127.0.0.1 --port 8080
```

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
├── notebooks/         # Jupyter notebooks for experimentation
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

## Model Experiments and Results

### Current Production Model
- **Architecture**: LaBSE Embeddings + Logistic Regression
- **Performance**:
  - Accuracy: 99%
  - Perfect separation of spam and non-spam messages
  - Robust performance on Swahili text
- **Advantages**:
  - Lightweight and fast inference
  - Excellent multilingual capabilities
  - Production-ready with minimal computational requirements
- **Disadvantages**:
  - Difficulty explaining individual predictions

### Model Comparison

| Model | Accuracy | Swahili Support | Explanation Quality | Notable Characteristics |
|-------|----------|-----------------|---------------------|------------------------|
| Qwen3 + LR | 100% | Excellent | N/A | Perfect accuracy, lightweight, production-ready |
| LaBSE + LR | 99% | Excellent | N/A | Fast, lightweight, production-ready |
| Qwen 3-4B | 96% | Good | Moderate | Strong at detecting financial scams |
| GPT-4.1 | 89% | Excellent | Outstanding | Best at Swahili explanations |
| Gemma 3-4B-IT | 79% | Moderate | Good | Good baseline performance |

### Topic Modeling Analysis

The project includes topic modeling using BERTopic to better understand the different types of spam messages. The analysis was performed using:
- **Embedding Model**: Sentence Transformers with LaBSE embeddings
- **Clustering**: HDBSCAN
- **Dimensionality Reduction**: UMAP

#### Identified Topics

Five distinct topics were identified in the spam messages:

1. **Topic 0**: Money-related scams
2. **Topic 1**: Financial fraud schemes
3. **Topic 2**: Phishing attempts (containing malicious links)
4. **Topic 3**: Traditional healing advertisements
5. **Topic 4**: Prize/reward scams (promising significant monetary rewards)

This topic modeling provides valuable insights into the different categories of spam messages in Swahili, helping to better understand and combat various types of fraudulent communications.

### Alternative Approaches Explored

#### Zero-Shot Classification with Gemma 3-4B-IT
- **Performance**:
  - Accuracy: 79%
  - Good interpretability of results
- **Key Findings**:
  - Shows promise for low-resource languages
  - No fine-tuning required
  - Trade-off between accuracy and explainability

#### Model Explainability
- **Method**: LLM-based explanation using Gemma 3-4B-IT
- **Results**:
  - 100% recall for spam messages
  - Provides human-readable explanations for classifications
- **Example**:
  ```text
  Input: "KARIBU FREEMASON UTIMIZE NDOTO..."
  Classification: Spam
  Explanation: "Message identified as spam due to:
  1. Suspicious organization recruitment
  2. Promise of dream fulfillment
  3. Typical scam message patterns"
  ```

#### Detailed Findings

1. **Qwen 3-4B**
   - **Strengths**:
     - High accuracy (96%) with zero-shot prompting
     - Strong detection of financial scams
     - Good at identifying suspicious phone numbers
   - **Limitations**:
     - Explanations sometimes miss Swahili context
     - Occasional misinterpretation of local terms

2. **GPT-4.1**
   - **Strengths**:
     - Best Swahili language understanding
     - Most detailed and accurate explanations
     - Excellent cultural context awareness
   - **Limitations**:
     - Lower accuracy (89%) due to over-trusting
     - Sometimes misclassifies verified-looking scams

3. **LLaMA 3**
   - Not evaluated due to insufficient Swahili language support

## Production Deployment Strategy

### Recommended Approach
- **Primary Classification**: LaBSE + Logistic Regression
  - High accuracy (99%)
  - Low latency
  - Minimal compute requirements

- **Explanation Generation**: GPT-4.1 or Qwen 3-4B
  - On-demand explanations
  - High-quality Swahili understanding
  - Flexible deployment options

### Scaling Considerations
- **High-accuracy Explanations**:
  - Larger GPT/Qwen variants for critical use cases
  - Reasoning models for model introspection
  - Potential for fine-tuning based on failure analysis

- **Cost Optimization**:
  - Mixture of Experts (MoE) architectures for larger models
  - Selective explanation generation
  - Caching common explanations

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
   - Run data processing pipeline: `python main.py` or `dvc repro`. If you are using the latter, run `dvc init` command first
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