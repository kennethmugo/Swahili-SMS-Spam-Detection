FROM python:3.10-slim-bullseye

WORKDIR /app

# Install dependencies first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and models
COPY src/ ./src/
COPY model/ ./model/
COPY app.py .

# Create non-root user for security
RUN useradd -m appuser && \
    chown -R appuser:appuser /app
USER appuser

# Set Python path
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]