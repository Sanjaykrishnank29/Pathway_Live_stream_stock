# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install system dependencies for Pathway and PDF processing
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Create the data directory and an empty output file so Streamlit doesn't crash on start
RUN mkdir -p data && touch data/ui_output.csv

# Expose the port Streamlit runs on
EXPOSE 8501

# Add /app to PYTHONPATH so modules are accessible
ENV PYTHONPATH=/app

# Start both Pathway and Streamlit using a single command
# The '&' runs pipeline.py in the background while dashboard.py runs in the foreground
CMD python3 src/backend/pipeline.py & streamlit run src/frontend/dashboard.py --server.port=8501 --server.address=0.0.0.0