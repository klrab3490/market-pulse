# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.10
FROM python:${PYTHON_VERSION}-slim as base

# Prevent Python from writing pyc files & APISv
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LLM_API=${LLM_API}
ENV NEWS_API_KEY=${NEWS_API_KEY}
ENV TWELVE_DATA_API_KEY=${TWELVE_DATA_API_KEY}

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Expose FastAPI's port
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
