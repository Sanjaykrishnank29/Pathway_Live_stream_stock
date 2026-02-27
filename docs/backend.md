# Backend Documentation - Pathway Data Pipeline

The backend of **Green Bharat: Live AI Market Intelligence** is powered by the [Pathway](https://pathway.com/) framework, which provides a high-performance, reactive engine for streaming data processing.

## Components

### 1. `src/backend/pipeline.py`
The orchestration layer that assembles the Pathway reactive graph using modular components.

### 2. `src/backend/models.py`
Contains the **`GreenAssetSchema`**, defining the structure of the incoming data.

### 3. `src/backend/streaming.py`
Encapsulates **`get_market_data_stream()`**, which simulates high-frequency sustainability market feeds.

### 4. `src/backend/utils.py`
Provides utility functions like **`create_esg_prompt()`** and advanced **`retry_llm_call`** decorators for robust API interaction.

### 5. `src/backend/analytics.py`
Contains domain-specific logic such as **`classify_esg_risk()`** and trend detection algorithms.

## AI Reasoning Layer
The pipeline uses `LiteLLMChat` from Pathway's LLM pack to interface with **Groq's Llama 3.1** models. The reasoning is performed asynchronously on the streaming data, providing real-time insights based on the ESG scores.

## Data Sink
Processed insights are written to `data/ui_output.csv`. This file acts as a low-latency intermediary between the backend streaming engine and the frontend dashboard.
